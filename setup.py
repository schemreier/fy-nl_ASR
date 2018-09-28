#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Frisian Dutch Automatic Speech Recognition Webservice",
    version = "0.1",
    author = "Emre Yılmaz",
    author_email = "emre@nus.edu.sg",
    description = ("Webservice"),
    license = "unknown",
    keywords = "clam webservice rest nlp computational_linguistics rest",
    url = "https://github.com/schemreier/fy-nl_ASR",
    packages=['fy_nl_ASR'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3"
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    package_data = {'fy_nl_ASR':['*.sh','*.wsgi','*.yml'] },
    include_package_data=True,
    install_requires=['CLAM >= 2.3']
)
