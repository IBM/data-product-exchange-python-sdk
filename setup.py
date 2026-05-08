#!/usr/bin/env python
# Copyright 2019, 2020 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os
import sys
import warnings

__version__ = '1.7.1'

PACKAGE_NAME = 'dph_services'
PACKAGE_DESC = '[DEPRECATED] Python client library for DPH Services - Please use ibm-data-intelligence-sdk instead: https://github.com/IBM/data-intelligence-sdk'

# Display deprecation warning during installation
warnings.warn(
    "\n" + "="*80 + "\n"
    "WARNING: This package (dph-services) is DEPRECATED and no longer maintained.\n"
    "\n"
    "Please migrate to the new package:\n"
    "  pip install ibm-data-intelligence-sdk\n"
    "\n"
    "New repository: https://github.com/IBM/data-intelligence-sdk\n"
    + "="*80,
    DeprecationWarning,
    stacklevel=2
)

def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

install_requires = read_requirements('requirements.txt')
tests_require = read_requirements('requirements-dev.txt')

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name=PACKAGE_NAME.replace('_', '-'),
    version=__version__,
    description=PACKAGE_DESC,
    license='Apache 2.0',
    install_requires=install_requires,
    extras_require={'test': tests_require},
    author='IBM',
    author_email='shashank.bhushan.jha@ibm.com',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/IBM/data-intelligence-sdk',
    packages=[PACKAGE_NAME],
    include_package_data=True,
    keywords=PACKAGE_NAME,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    deprecated=True,
    zip_safe=True,
)