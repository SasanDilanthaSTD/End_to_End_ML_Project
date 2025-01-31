import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
__version__ = "0.0.0"

REPO_NAME = "End_to_End_ML_Project"
AUTHOR_USERNAME = "SasanDilanthaSTD"
SRC_REPO = "RedWineQualityPrediction"
AUTHOR_EMAIL = "sasandilantha12@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to predict the quality of red wine",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
        },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)