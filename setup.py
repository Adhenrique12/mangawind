#!/usr/bin/env python

from distutils.core import setup

setup(name='MangaWind',
      version='2.0.0',
      description='a manga downloader',
      url='https://github.com/Adhenrique12/mangawind',
      platforms='Unix',
      license='MIT',
      py_modules=['lxml', 'bs4', 'pyyaml', 'progress', 'cloudscraper']
     )