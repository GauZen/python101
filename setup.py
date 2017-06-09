#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
import ast
import re

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open(os.path.join(root_dir, 'python101', '__init__.py'), 'r') as f:
    version = str(ast.literal_eval(_version_re.search(f.read()).group(1)))


setup(
    name='python101',
    version=version,
    packages=find_packages(),
    url='https://github.com/ZeeD26/python101',
    license='BSD',
    author='Dominik Steinberger',
    author_email='dominik.steinberger@imfd.tu-freiberg.de',
    description='Python tutorial for computational materials scientists.',
    install_requires=[
        'Sphinx',
        'sphinx_rtd_theme',
        'numpy',
        'matplotlib',
        'scipy',
        'pytest'
    ])
