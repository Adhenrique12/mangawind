from setuptools import setup

setup(
    name="mangawind",
    version="0.1.0",
    py_modules=["app", "manga_manipulation", "downloader"],
    install_requires=[
        'Click', 'requests', 'bs4', 'Pillow', 'progress'
    ],
    entry_points='''
    [console_scripts]
    mangawind=app:main
    ''',
)