from setuptools import setup, find_packages
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='bmdOilPriceFetch',
    version='0.6.1',
    author='Benjamin M. Duivesteyn',
    author_email='duivesteyn@gmail.com',
    packages=['bmdOilPriceFetch'],
    url='https://github.com/duivesteyn/bmdOilPriceFetch',
    license='LICENSE',
    description='A Fast and Efficient way to get the current Oil Price from Yahoo Finance API in Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    scripts=['test.py'],
    include_package_data = True,
    classifiers=[ "Programming Language :: Python :: 3", "Programming Language :: Python :: 3.7",
    ]
)