#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='worldmap',
    version='0.1.0',
    packages=find_packages('src'),
    package_data={},
    package_dir={'': 'src'},
    entry_points={'console_scripts': [
            'worldmap-plot = worldmap.utils.mpl_map_plot:main'
        ]},
)
