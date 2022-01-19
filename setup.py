# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "finnhub-python"
VERSION = "2.4.8"
REQUIRES = ["requests >= 2.22.0"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Finnhub API",
    author="Finnhub",
    author_email="support@finnhub.io",
    url="https://finnhub.io/docs/api",
    keywords=["finnhub", "Finnhub API", "api"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown"
)
