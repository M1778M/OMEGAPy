from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("ETU_DLL",  ["etu.py"]),
]

setup(
    name = 'etu_dll',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
