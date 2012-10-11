#!/usr/bin/env python

"""
distutils/setuptools install script. See inline comments for packaging documentation.
"""

import os
import sys

try:
  from setuptools import setup
  # hush pyflakes
  setup
except ImportError:
  from distutils.core import setup

try:
  from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
  from distutils.command.build_py import build_py

packages = []

package_dir = {}

package_data = {}

scripts = [
  'catarc'
]


setup(
  name='catarc',
  version='1.1',
  maintainer='Sven Slootweg',
  maintainer_email='admin@cryto.net',
  description='Tool to output uncompressed contents of (multiple) archives to stdout, without writing to disk',
  url='http://www.cryto.net/projects/catarc/',
  packages=packages,
  package_dir=package_dir,
  package_data=package_data,
  include_package_data=True,
  scripts=scripts,
  install_requires=['argparse'],
  cmdclass={'build_py': build_py}
)

