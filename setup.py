#!/usr/bin/env python

from __future__ import absolute_import
from distutils.core import setup

# Write this to
version = "0.1"

setup(name='nplook',
    version=version,
    author="Gustav Larsson",
    author_email="gustav.m.larsson@gmail.com",
    url="http://github.com/gustavla/nplook",
    description="Command-line tool that peeks into a numpy NPZ file and summarizes the contents",
    install_requires=['PIL'],
#    long_description="Tool for evaluating and analysing eye movement classification algorithms."
    packages=['nplook'],
    scripts=['scripts/nplook'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
