from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Blooker",
    version="0.1",
    author="Biggie",
    author_email="thugshaker@yahoo.com",
    description="Flood Blooket Games",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bigboy-baby/"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3',
)