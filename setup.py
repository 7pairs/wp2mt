# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from wp2mt import __version__


setup(
    name='wp2mt',
    version=__version__,
    description='Tools for converting WordPress to Movable Type',
    author='Jun-ya HASEBA',
    author_email='7pairs@gmail.com',
    url='http://seven-pairs.hatenablog.jp/',
    packages=find_packages(),
    install_requires=['beautifulsoup4'],
    entry_points="""\
    [console_scripts]
    wp2mt = wp2mt.wp2mt:main
    """
)
