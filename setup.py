#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup process."""

from io import open
from os import path

from setuptools import find_packages, setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'),
          encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Basic project information
    name='airflow-xcom-redis',
    version='0.1.0',
    # Authorship and online reference
    author='Jakub Sokołowski',
    author_email='jakub@status.im',
    url='https://github.com/status-im/airflow-xcom-redis',
    # Detailled description
    description='Alternative Backend for Airflow XCom.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='airflow xcom backend redis',
    # Package configuration
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    python_requires='>= 3.6',
    install_requires=[],
    # Licensing and copyright
    license='Apache 2.0'
)
