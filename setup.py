from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="webir",
    version="0.1.0",
    author="Jose Bujalance",
    author_email="joseab56@gmail.com",
    description="A REST-like web interface to a local LIRC daemon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jbujalance/webir",
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.2',
        'py-irsend==1.0.2',
        'flask-of-oil==1.1.0'
    ],
    python_requires='>=3.7',
)
