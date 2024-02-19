from setuptools import setup, find_packages, Extension

import sys
import os

mytest_version = "0.1.0"

# Build and distribute without cython and .pyx files:
# cf. https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
try:
    from Cython.Build import cythonize
    use_cython = True
except ImportError:
    use_cython = False

# Sources
Include_dirs = [ "./mytest" ]

extensionParams = {
    "language":"c++",
    "include_dirs":Include_dirs,
    }

extension_names = [
    'my_cython_class',
    ]

use_cython_ext = '.pyx' if use_cython else '.cpp'

extensions = [
    Extension('mytest.'+f,
              sources = [ 'mytest/'+f+use_cython_ext ],
              **extensionParams)
    for f in extension_names
]

packages = find_packages(".")

if use_cython:
    from Cython.Build import cythonize
    extensions = cythonize(extensions,
                           # language_level=3,
                           nthreads=8)


## Finally, do the setup
setup(
    name = "mytest",
    version = mytest_version,
    packages = packages,
    ext_modules = extensions,
    )
