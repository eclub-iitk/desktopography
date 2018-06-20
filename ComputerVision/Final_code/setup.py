from distutils.core import setup

from Cython.Build import cythonize





setup(name = "cythontry",

    ext_modules = cythonize("cythontry.pyx")

)

