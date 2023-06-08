import os
from git import Repo
from pathlib import Path
import shutil
from bs4 import BeautifulSoup as Soup

# Set the API Key for OpenAI (If required)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Set path for blog repository
PATH_TO_BLOG_REPO: Path = Path('/Users/jonchristie/Desktop/WEB_DEV_DOCS/CLONED_REPOS/ai-blog/')

PATH_TO_CONTENT = PATH_TO_BLOG_REPO / "content"

PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)

# Create a function for updating the blog
def update_blog(commit_message="Updates Blog"):
    # GitPython -- Repo Location
    repo = Repo(PATH_TO_BLOG_REPO)
    # git add .
    repo.git.add(all=True)
    #  git commit -m "updates blogs"
    repo.index.commit(commit_message)
    # git push
    origin = repo.remote(name="origin")
    origin.push()

def create_new_blog(title, content, cover_image):
    cover_image = Path(cover_image)

    # Automatic file naming system
    files = len(list(PATH_TO_CONTENT.glob("*.html")))
    new_title = f"{files + 1}.html"
    path_to_new_content = PATH_TO_CONTENT / new_title

    shutil.copy(cover_image, PATH_TO_CONTENT)

    if not os.path.exists(path_to_new_content):
        # Write new HTML file
        with open(path_to_new_content, "w") as f:
            f.write('<!DOCTYPE HTML>\n<html>\n<head>\n')
            f.write(f"<title> {title} </title>\n</head>\n<body>\n")
            f.write(f"<img src='{cover_image.name}' alt='Cover Image'> <br/>\n")
            f.write(f"<h1>{title}</h1>\n")
            # Add new content by taking openai's \n and replacing them with breaks
            f.write(content.replace("\n", "<br />\n"))
            f.write("</body>\n</html>\n")
            print("Blog Created")
            return path_to_new_content

    else:
        raise FileExistsError("File already exists, please check the name again. Aborting now!")

# Create a new blog
path_to_new_content = create_new_blog('Test_title', 'test content test content', './jCircle128x128.png')

# Update the blog after creating the new blog
update_blog()

# Update index.html ---> Blog Posts
with open(PATH_TO_BLOG_REPO/"index.html") as index:
    soup = Soup(index.read(), features="lxml")

print(str(soup))
print(soup.prettify())

# Check for duplicate links
def check_for_duplicate_links(path_to_new_content, links):
    urls = [str(link.get("href")) for link in links] # [1.html, 2.html, 3.html]
    content_path = str(Path(*path_to_new_content.parts[-2:]))
    # blog you just created is going to be "../1.html"
    return content_path in urls
# Write the blog post link to index.html file
def write_to_index(path_to_new_content):
    with open(PATH_TO_BLOG_REPO/'index.html') as index:
        soup = Soup(index.read())

    # find all the links and get the very last link
    links = soup.find_all('a')
    last_link = links[-1]

    if check_for_duplicate_links(path_to_new_content, links):
        raise ValueError("Link already exists")

    # Finding the path to the new content
    link_to_new_blog = soup.new_tag("a",href=Path(*path_to_new_content.parts[-2:]))
    # convert to a string and insert the last link right after that link to the new blog
    link_to_new_blog.string = path_to_new_content.name.split('.')[0]
    last_link.insert_after(link_to_new_blog)

    with open(PATH_TO_BLOG_REPO/'index.html','w') as f:
        f.write(str(soup.prettify(formatter='html')))

write_to_index(path_to_new_content)

update_blog()