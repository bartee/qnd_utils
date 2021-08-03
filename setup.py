#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Bart Stroeken",
    author_email='bart.stroeken@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is a set of utilities for quick and dirty data extraction processes from CSVs and json files",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='qnd_utils',
    name='qnd_utils',
    packages=find_packages(include=['qnd_utils', 'qnd_utils.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bartee/qnd_utils',
    version='0.1.0',
    zip_safe=False,
)
