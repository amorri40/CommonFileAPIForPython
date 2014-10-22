import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "CommonFileAPIForPython",
    version = "0.0.1",
    author = "Alasdair Morrison",
    author_email = "amorri40@gmail.com",
    description = ("Functions to make file handling even easier!"),
    license = "BSD",
    keywords = "common file database sqlite",
    url = "http://packages.python.org/CommonFileAPIForPython",
    packages=['CommonFileAPI'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)