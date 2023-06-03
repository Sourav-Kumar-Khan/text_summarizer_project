import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USERNAME = "Sourav-Kumar-Khan"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "khansourav1999@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USERNAME + "/" + SRC_REPO,
    project_url={
        "Bug Tracker": "https://github.com/" + AUTHOR_USERNAME + "/" + SRC_REPO + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)