#!/usr/bin/env python

import os

from setuptools import setup, find_packages

setup(
    name='clcache',
    description='MSVC compiler cache',
    author='Frerich Raabe',
    author_email='raabe@froglogic.com',
    url='https://github.com/frerich/clcache',
    packages=find_packages(),
    platforms='any',
    keywords=[],
    install_requires=[
        'typing; python_version < "3.5"',
        'subprocess.run; python_version < "3.5"',
        'atomicwrites',
        'pymemcache',
        'pyuv @ git+https://github.com/saghul/pyuv@2a3d42d44c6315ebd73899a35118380d2d5979b5#egg=pyuv',
    ],
    entry_points={
          'console_scripts': [
              'clcache = clcache.__main__:main',
              'cl.cache = clcache.__main__:main',
              'clcache-server = clcache.server.__main__:main',
          ]
    },
    setup_requires=[
        'setuptools_scm',
    ],
    data_files=[
        ('', ('clcache.pth',)),
    ],
    use_scm_version=True)
