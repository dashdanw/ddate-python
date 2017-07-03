#!/usr/bin/env python3

from distutils.core import setup, Extension
import ddate
import pypandoc

setup(
    name="ddate",
    packages=[
        'ddate'
    ],
    install_requires=[
        'setuptools',
        'Django>=1.8'
    ],
    version=ddate.__version__,
    description='ddate C bindings',
    author='Dash Winterson',
    author_email='dashdanw@gmail.com',
    url='https://github.com/dashdanw/ddate-python',
    download_url='https://github.com/dashdanw/ddate-python/archive/{}.tar.gz'.format(ddate.__version__),
    keywords=[
        'ddate',
        'linux',
        'util',
        'linux-util'
    ],
    classifiers=[],
    long_description=pypandoc.convert('README.md', 'rst'),
    ext_modules=[Extension("cddate", ["bind.c", "libddate.c"])]
)