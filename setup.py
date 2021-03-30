from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="soccer-data-api",
    version="0.5.3",
    description="A Python web-scrap package to get soccer data/stats.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/reppon97/soccer-data-api",
    author="Rejep Mammedov",
    author_email="reppon97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=['soccer_data_api'],
    include_package_data=True,
    install_requires=[
        'beautifulsoup4==4.9.1', 'chardet', 'idna', 'requests', 'urllib3'
    ],

)
