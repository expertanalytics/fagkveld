#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="bokeh-worldmap",
    version="0.1.0",
    packages=find_packages("src"),
    package_data={},
    package_dir={"": "src"},
    entry_points={"console_scripts": []},
)
