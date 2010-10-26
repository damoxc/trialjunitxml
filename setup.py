#!/usr/bin/python
#
# trialjunitxml -- plugin to integrate junitxml with Twisted trial.
#
# Author: Damien Churchill
#

import os
import re
import sys

from setuptools import find_packages, setup

data_files = [(os.path.join('twisted', 'plugins'), [os.path.join('twisted', 'plugins', 'trialcoveragereporterplugin.py')])]

setup(
    name         = 'trialjunitxml',
    version      = '0.0.1',
    description  = 'A plugin to integrate junitxml with Twisted trial.',
    author       = 'Damien Churchill',
    author_email = 'damoxc@gmail.com',
    url          = 'http://github.com/damoxc/vmail',
    license      = 'GPLv3',

    packages     = find_packages(),
    include_package_data = True,
    zip_safe     = False,
    install_requires = ['setuptools'],
    data_files   = data_files,
    test_suite   = 'trialcoverage.test'
)
