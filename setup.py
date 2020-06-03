from setuptools import setup, find_packages  # noqa: H301

NAME = "finnhub-python"
VERSION = "1.0.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Finnhub API",
    author="OpenAPI Generator community",
    author_email="support@finnhub.io",
    url="https://finnhub.io/docs/api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["OpenAPI", "OpenAPI-Generator", "Finnhub API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
)
