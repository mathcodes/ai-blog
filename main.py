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