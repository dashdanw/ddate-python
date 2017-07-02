#!/usr/bin/env python3

from distutils.core import setup, Extension

setup(
    name = "ddate",
    version = "1.0",
    ext_modules = [Extension("ddate", ["bind.c", "libddate.c"])]
    );
