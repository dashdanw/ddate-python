#!/usr/bin/env python3

from distutils.core import setup, Extension
import ddate

setup(
    name="ddate",
    packages=[
        'ddate'
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
    long_description="C binding for oldschool util-linux ddate.",
    ext_modules=[Extension("cddate", ["cddate/bind.c", "cddate/libddate.c"])]
)