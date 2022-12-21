#WARNING: this is not all of metohds of stdlib.h
import numpy
from .cext import *

def malloc(size_t):
    return (numpy.array(['\x00']*size_t))
def calloc(m,type_):
    return numpy.array(['\x00']*(sizeof(type_)*m))

class BIN:
    NONETYPED_OBJECT = type(None)
    NONEFORMAT = None


