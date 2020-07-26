from setuptools import find_packages, setup  # type: ignore
from setuptools.extern import packaging  # type: ignore

from shape_bruteforce import __version__
version = __version__

# Add readme as long description
with open("README.md") as f:
    long_description = f.read()

# Library dependencies
INSTALL_REQUIRES = [
    "pycairo",
]

setup(
    name="shape_bruteforce",
    version=version,
    description="Generate art using simple geometric shapes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedkhalf/Shape-Bruteforce/",
    packages=find_packages(),
    author="Ahmed Khalf",
    author_email="ahmedkhalf567@gmail.com",
    setup_requires=["wheel"],
    entry_points={"console_scripts": ["shape-bruteforce=shape_bruteforce.main:main"]},
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
)
