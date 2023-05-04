from setuptools import setup, find_packages

setup(
    name="catt",
    version="0.12.10",
    packages=["catt"],
    install_requires=[
        "Click>=6.7",
        "PyChromecast>=12.1.4",
        "typing; python_version<'3.5'",
        "setuptools>=40.0.0",
    ],
)
