#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2015 Jun-ya HASEBA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import find_packages, setup

from wp2mt import __version__


setup(
    name='wp2mt',
    version=__version__,
    description='Tools for converting WordPress export file to Movable Type format',
    author='Jun-ya HASEBA',
    author_email='7pairs@gmail.com',
    url='https://github.com/7pairs/wp2mt',
    packages=find_packages(),
    install_requires=['beautifulsoup4'],
    entry_points="""\
    [console_scripts]
    wp2mt = wp2mt.wp2mt:main
    """
)
