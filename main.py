import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

from git import Repo

from pathlib import Path


# create function for updating blog that adds anything new, commits it and pushes it
# ALso create a function that sets up simple html file with inserts for actual call for whatever content we want to insert there

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

random_text_string = "!@#$M!F!#$~!!#$"
PATH_TO_BLOG_REPO = Path('/Users/jonchristie/Desktop/WEB_DEV_DOCS/CLONED_REPOS/ai-blog/')

PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent


PATH_TO_CONTENT = PATH_TO_BLOG/"content"


PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)

with open(PATH_TO_BLOG/"index.html", 'w') as f:
  f.write(random_text_string)

update_blog()

import shutil
def create_new_blog(title,content,cover_image):
  cover_image = Path(cover_image)

  # automatic file naming system
  files = len(list(PATH_TO_CONTENT.glob("*.html")))
  new_title = f"{files+1}.html"
  path_to_new_content = PATH_TO_CONTENT/new_title

  shutil.copy(cover_image, PATH_TO_CONTENT)

  if not os.path.exists(path_to_new_content) :
    # write new html file
    with open(path_to_new_content, "w") as f:
      f.write('<!DOCTYPE HTML>\n')
      f.write("<html>\n")
      f.write("<head>\n")
      f.write(f"<title> {title} </title>\n")
      f.write("</head>\n")

      f.write("<body>\n")
      f.write(f"<img src='{cover_image.name}' alt='Cover Image'> <br/>\n")
      f.write(f"<h1>{title}</h1>\n")
      # add new content by taking openai's \n and replacing them with breaks
      f.write(content.replace("\n","<br />\n"))
      f.write("</body>\n")
      f.write("<html>\n")
      print("Blog Created")
      return path_to_new_content

  else:
    raise FileExistsError("File already exists, please check the name again. Aborting now!")

path_to_new_content = create_new_blog('Test_title', 'test content test content', './jCircle128x128.png')