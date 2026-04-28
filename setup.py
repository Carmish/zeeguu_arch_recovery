# Installing Required Dependencies
import sys

sys.version
# Install GitPython and PyVis if not already installed
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "gitpython"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyvis"])

import os

# Get the name of the folder where our script runs:
cwd = os.getcwd()

# Declare a var for the path where we're going to download a repository:
CODE_ROOT_FOLDER = cwd + "/zeeguu-api/"
from git import Repo

# GitPython is a library that allows us to work easily with git from Python
# https://gitpython.readthedocs.io/en/stable/tutorial.html


# If the file exists, it means we've already downloaded
if not os.path.exists(CODE_ROOT_FOLDER):
    Repo.clone_from("https://github.com/zeeguu/api", CODE_ROOT_FOLDER)


def file_path(file_name):
    """Helper function to get the full path of a file in the code repository."""
    return CODE_ROOT_FOLDER + file_name


def module_name_from_file_path(full_path):
    """Convert file path to module name.
    Example: ../core/model/user.py -> zeeguu.core.model.user
    """

    file_name = full_path[len(CODE_ROOT_FOLDER) :]
    file_name = file_name.replace("/__init__.py", "")
    file_name = file_name.replace("/", ".")
    file_name = file_name.replace(".py", "")
    return file_name
