from distutils.core import setup, Extension
import numpy
# define the extension module
DTW = Extension('DTW', sources=['DTW.c'])

# run the setup
setup(ext_modules=[DTW])

