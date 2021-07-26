import re
from setuptools import setup, find_packages
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def find_version(*file_path_parts):
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, *file_path_parts), "r") as fp:
        version_file_text = fp.read()

    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")



setup(
    name="pyverrt",
    version=find_version("pyverrt", "__init__.py"),
    description="Python version release test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[],
    author="Byungchan Kim",
    author_email="kbc8894@gmail.com",
    url=[],
    keywords=["python", "version"],
    packages=find_packages(),
    install_requires=[],
)
