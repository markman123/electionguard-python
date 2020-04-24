#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

NAME = "electionguard"
VERSION = "0.1.0"
LICENSE = "MIT"
DESCRIPTION = "ElectionGuard: Support for e2e verified elections."
AUTHOR = "Dan S. Wallach"
AUTHOR_EMAIL = "dwallach@gmail.com"
URL = "https://github.com/microsoft/electionguard-python"
PROJECT_URLS = {
    "Changelog": "https://github.com/microsoft/electionguard-python/blob/master/CHANGELOG.rst",
    "Issue Tracker": "https://github.com/microsoft/electionguard-python/issues",
}
CLASSIFIERS = [
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: Unix",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Utilities",
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    project_urls=PROJECT_URLS,
    python_requires=">=3.8",
    install_requires=["gmpy2==2.1.0b4"],
)
