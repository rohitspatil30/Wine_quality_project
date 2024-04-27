import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "wine_quality_project"
AUTHOR_USER_NAME = 'rohitspatil30'
SRC_REPO = 'wine_quality_prediction'
AUTHOR_EMAIL = "rohitspatil30@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for predicting wine quality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohitspatil30/wine_quality_project",
    packages = setuptools.find_packages(where="src"),
    project_urls={
        "Bug Tracker": "https://github.com/rohitspatil30/wine_quality_project/issues",
    },
    package_dir={'': 'src'},
    
)

