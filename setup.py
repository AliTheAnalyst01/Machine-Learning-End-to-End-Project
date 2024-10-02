import setuptools


__version__ ='0.0.0'

REPO_NAME = "Machine-Learning-End-to-End-Project"
AUTHOR_USER_NAME = "AliTheAnalyst"
SRC_REOP = "MLProject_WineQT"
AUTHOR_EMAIL="faizanzaidy78@gmail.com"

setuptools.setup(
    name=SRC_REOP,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='a small python package for ml app',
    url=f"https:\\github.com\{AUTHOR_USER_NAME}\{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https:\\github.com\{AUTHOR_USER_NAME}\{REPO_NAME}\issues"
    },
    package_dir={'':'src'},
    packages= setuptools.find_packages(where='src')
)