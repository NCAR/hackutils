#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.rst') as f:
    long_description = f.read()

setup(
    maintainer='NCAR XDev Team',
    maintainer_email='xdev@ucar.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='sandbox utilities',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description=long_description,
    include_package_data=True,
    keywords='hackutils',
    name='hackutils',
    packages=find_packages(include=['hackutils', 'hackutils.*']),
    url='https://github.com/NCAR/hackutils',
    project_urls={
        'Documentation': 'https://github.com/NCAR/hackutils',
        'Source': 'https://github.com/NCAR/hackutils',
        'Tracker': 'https://github.com/NCAR/hackutils/issues',
    },
    zip_safe=False,
)
