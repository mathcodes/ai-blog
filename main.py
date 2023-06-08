import os
import openai
from git import Repo
from pathlib import Path
import shutil
from bs4 import BeautifulSoup as Soup
import requests

# Set the API Key for OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

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


# Create a new blog
def create_new_blog(title, content, cover_image):
    cover_image = Path(cover_image)
    shutil.copy(cover_image, PATH_TO_CONTENT)

    # Automatic file naming system
    files = len(list(PATH_TO_CONTENT.glob("*.html")))
    new_title = f"{files + 1}.html"
    path_to_new_content = PATH_TO_CONTENT / new_title

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
            return new_title

    else:
        raise FileExistsError("File already exists, please check the name again. Aborting now!")


# Write the blog post link to index.html file
def write_to_index(blog_filename):
    with open(PATH_TO_BLOG_REPO / 'index.html') as index:
        soup = Soup(index.read())

    # find all the links
    links = soup.find_all('a')

    content_path = f"../{blog_filename}"
    if content_path in [str(link.get("href")) for link in links]:
        raise ValueError("Link already exists")

    # Finding the path to the new content
    link_to_new_blog = soup.new_tag("a", href=content_path)
    link_to_new_blog.string = blog_filename.split('.')[0]

    if len(links) == 0:  # if no links exist yet
        soup.body.append(link_to_new_blog)  # add the new link to the body
    else:  # if some links already exist
        links[-1].insert_after(link_to_new_blog)  # add the new link after the last one

    with open(PATH_TO_BLOG_REPO / 'index.html', 'w') as f:
        f.write(str(soup.prettify(formatter='html')))


# Generate a blog post using OpenAI's GPT-3
def generate_blog_post(title):
    prompt = """
        Biography:
        My name is Jon and I am a full stack instructor for coding.

        Blog
        Title: {}
        tags: tech, frontend, backend, fullstack, webdevelopment
        Summary: I talk about what the future of AI brings to Web Development
        Full Text.""".format(title)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()


# Generate an image using OpenAI's DALL-E
def generate_image(title):
    prompt = f"3d clay abstract metaphor of {title}"
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response['data'][0]['url']
    return image_url


# Save image from URL
def save_image(image_url, file_name):
    image_res = requests.get(image_url, stream=True)

    if image_res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(image_res.raw, f)
    else:
        print("Error downloading image!!")
    return file_name


# Generate blog content and image
title = "The future of Web Development and AI"
blog_content = generate_blog_post(title)
image_url = generate_image(title)
image_filename = save_image(image_url, file_name="title2.png")

# Create new blog
blog_filename = create_new_blog(title, blog_content, image_filename)

# Update index and push to git
write_to_index(blog_filename)
update_blog()
