# AI Blog Script

- Programming Languages and Technologies:
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&style=for-the-badge)](https://www.python.org/) [![HTML](https://img.shields.io/badge/HTML-5-%23E34F26?logo=html5&style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/HTML) [![CSS](https://img.shields.io/badge/CSS-3-%231572B6?logo=css3&style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-%23F37626?logo=jupyter&style=for-the-badge)](https://jupyter.org/) [![Markdown](https://img.shields.io/badge/Markdown-1.0-%23000000?logo=markdown&style=for-the-badge)](https://daringfireball.net/projects/markdown/)

- Frameworks and Libraries:
[![Tailwind CSS](https://img.shields.io/badge/Framework-Tailwind%20CSS-%2338B2AC?logo=tailwind-css&style=for-the-badge)](https://tailwindcss.com/) [![shutil](https://img.shields.io/badge/module-shutil-%230D1117?logo=git&style=for-the-badge)](https://docs.python.org/3/library/shutil.html) [![Path](https://img.shields.io/badge/class-Path-%230D1117?logo=git&style=for-the-badge)](https://docs.python.org/3/library/pathlib.html) [![GitPython](https://img.shields.io/badge/dependency-GitPython-%230D1117?logo=git&style=for-the-badge)](https://github.com/gitpython-developers/GitPython) [![BeautifulSoup](https://img.shields.io/badge/dependency-BeautifulSoup4-%234285F4?logo=git&style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)

- Development Tools and APIs:
[![Git](https://img.shields.io/badge/version_control-Git-%23121011?logo=git&style=for-the-badge)](https://git.com/) [![OpenAI API](https://img.shields.io/badge/OpenAI%20API-v1.0-%230075FF?logo=openai&style=for-the-badge)](https://openai.com/)

- AI and Machine Learning:
[![Language Model](https://img.shields.io/badge/Language%20Model-GPT--3.5-%23FFD54F?logo=openai&style=for-the-badge)](https://openai.com/) [![NLP](https://img.shields.io/badge/tech-NLP-%230075FF?logo=openai&style=for-the-badge)](https://en.wikipedia.org/wiki/Natural_language_processing) [![ML](https://img.shields.io/badge/tech-ML-%23FF6F00?logo=openai&style=for-the-badge)](https://en.wikipedia.org/wiki/Machine_learning) [![AI](https://img.shields.io/badge/tech-AI-%23239120?logo=openai&style=for-the-badge)](https://en.wikipedia.org/wiki/Artificial_intelligence)


This script automates the process of creating and updating a blog using AI-generated content and images. It leverages the OpenAI API for generating blog content and images, GitPython for managing the blog repository, and BeautifulSoup for manipulating HTML files.

## Example Output:

<img src="./example.png"  width="50%" alt="Example of generated HTML file">

## Prerequisites

Before using the script, ensure that you have the following:

- Python 3 installed on your system.
- OpenAI API key: You need to have a valid OpenAI API key to generate blog content and images. Visit the OpenAI website to obtain an API key.
- GitPython: Install the GitPython library by running `pip install GitPython`.
- BeautifulSoup: Install the BeautifulSoup library by running `pip install beautifulsoup4`.
- Tailwind CSS: The generated HTML files are styled using Tailwind CSS. The required stylesheets are loaded from the CDN, so an internet connection is necessary.

## Setup

1. Clone the AI blog repository:

```bash
git clone <repository-url>
```

2. Set the environment variable:

```bash
export OPENAI_API_KEY=<your-api-key>
```
Replace <your-api-key> with your actual OpenAI API key.


### Customize the repository path:

In the script, modify the PATH_TO_BLOG_REPO variable to point to the local path of your cloned AI blog repository.

## Install dependencies:

```bash
pip install openai requests
```

### Usage
The script performs the following steps:

Generate blog content and image using the OpenAI API.
Save the image locally.
Create a new blog HTML file.
Update the index HTML file with the link to the new blog.
Commit and push the changes to the Git repository.
To use the script, simply run it:

```python
python main.py
```

Make sure you are in the same directory as the main.py file.

### Generated HTML Style
As shown above, the generated HTML files have a simple design as the main point of this project was getting the backend to work. Each card contains the blog title, cover image, and content.

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License.



This README provides a comprehensive guide to the AI blog script, including prerequisites, setup instructions, usage details, generated HTML style, contribution guidelines, and license information. The code snippets and image are preserved, and line-by-line explanations are added within the code blocks.

## Contact
<img src ="https://avatars0.githubusercontent.com/u/17928947?v=4" alt="Github profile image" width="80px" height="80px" />

__Jon Christie__



[![Twitter](https://img.shields.io/badge/Twitter-follow-%2327a1f2?style=for-the-badge&logo=twitter)](https://twitter.com/jCircle9)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jonpchristie-%23156599?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/jonpchristie)
[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC5GFnN-lv8Yuqc9O3b79k6g?style=for-the-badge&logo=youtube&color=fe0000)](https://www.youtube.com/channel/UC5GFnN-lv8Yuqc9O3b79k6g)
[![Hashnode](https://img.shields.io/badge/Hashnode-Tech_Blog-%232196F3?style=for-the-badge&logo=hashnode&color=2962ff)](https://hashnode.com/@jcircle9)
[![Instagram Follow](https://img.shields.io/badge/Instagram-Follow-%23db11a9?style=for-the-badge&logo=instagram)](https://www.instagram.com/jcirclenine/)


