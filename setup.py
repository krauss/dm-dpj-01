""" Proxy Scrapper CLI setup.py
"""
from setuptools import setup, find_packages

setup(
    name="prox_crapper",
    version="0.1.0",
    description="Proxy scrapper command-line interface (CLI) for SeniorUp Job Test",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "lxml",
        "requests_futures"
    ],
    entry_points={
        'console_scripts': ['prox_crapper=src.main:main']
    },
    author="Krauss",
    license="MIT"
)