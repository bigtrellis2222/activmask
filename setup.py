#!/usr/bin/env python
import os
from setuptools import setup


setup(
    name='activmask',
    description='A way to get your CNN to ignore predictive features.',
    version='1.0',
    author='???',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'activmask = activmask.main:main'
        ]
    }

)
