##############################################################################
#
# Copyright (c) Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for cipher.session package
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='cipher.session',
    version='1.0.4',
    url="http://pypi.python.org/pypi/cipher.session/",
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description="A ZODB Session handling implementation",
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    license='ZPL 2.1',
    keywords="CipherHealth session",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    extras_require=dict(
        test=['zope.app.testing',
                'coverage',
                ],
        # ZODB bootstrap helper
        bootstrap=[
                'transaction',
                'zope.processlifetime',
                'zope.app.appsetup',
                ],
        # conflict aware / comparable credentials
        credentials=[
                'zope.pluggableauth',
                ]
    ),
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.component',
        'zope.session',
        'zope.location',
        'zope.publisher',
        'repoze.session',

    ],
    include_package_data=True,
    zip_safe=False
    )
