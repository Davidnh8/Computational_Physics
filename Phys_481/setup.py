from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("assignment_4_cython_new1.pyx"),
	include_dirs=[numpy.get_include()]
)