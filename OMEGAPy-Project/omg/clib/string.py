#WARNING: this is not all of metohds of string.h
from .cext import *


def strcat(str1,str2):
    return str1+str2

def strlen(string):
    return len(string)

def strcmp(str1,str2):
    if str1==str2:
        return 1
    else:
        return 0




