import os
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-nmb",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    author="Medson Naftali",
    author_email="medsonnaftal@gmail.com",
    description="Django app for NMB BANK Merchant payment gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devmed/django-nmb",
    project_urls={
        "Bug Tracker": "https://github.com/devmed/django-nmb/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        # And include any *.csv files found in the "mikoa" directory
    }
)