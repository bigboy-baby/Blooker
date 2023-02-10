from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="Blooker",
    version="0.0.3",
    author="Biggie",
    author_email="thugshaker@yahoo.com",
    description="Flood Blooket Games",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bigboy-baby/",
    packages=find_packages(),
    install_requires=['requests','websocket'],
    python_requires='>=3',
)
