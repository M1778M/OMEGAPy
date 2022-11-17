from .tools import listTool as LT
from libc.stdlib cimport malloc,free
import math
import sys


NumberSupports = [
    "16BIT_INTEGER_FLOAT"
    ,"8BIT_INTEGER_FLOAT"
    ,"4BIT_INTEGER_FLOAT"
    ,"32BIT_INTEGER"
    ,"64BIT_STDOMG_INTEGER_FLOAT"
    ,"128BIT_STDOMG_CHAR_STR_INTEGER_FLOAT_X"
    ]




class UnderSquareRoot:
    def __init__(self,y,x=2):
        (self.y,self.nus) = y
        self.x = x
        if x == 0:
            raise AttributeError('Attribute x cannot be 0')
        self.answer = y**(1/x)
    def undersqrt(self):
        return f'sqrt({y}, {x})'
    def __repr__(self):
        return f'sqrt({y}, {x})'
        
        

pi = math.pi


usqrt = UnderSquareRoot

def N(number):
    if number >= 1:
        return number
    else:
        return False
        

def W(number):
    if number >= 0:
        return number
    else:
        return False

def Z(number):
    if int(number) == number or type(number) == int:
        return number
    else:
        return False

def Q(number):
    if type(number) != UnderSquareRoot:
        if type(number) == float:
            if len(str(number).split('.')[-1])>5:
                return False
        return number
    else:
        if Z(number.answer):
            return number
        else:
            return False


def Qp(number):
    if type(number) == UnderSquareRoot:
        if len(str(number.answer).split('.')[-1])>5:
            return number
        else:
            return False
    elif type(number) == float:
        return number if len(str(number).split('.')[-1])>5 else False
    else:
        return False


def qzz(vi):
    return vi**(math.pi/-vi)
    



def rotaten(n,sub):
    # return's -(n*sub)*2
    return -(abs(n))*(sub/0.5)

def rotatin(*ns,sub):
    # rotatin(3,3,sub=3)
    #
    # 3*3*4+(3*4)
    #
    # ns1*ns2*sub+(lenOfInput,sub)   # LenOfInput = n(3,3,4) = 3
    return -(abs(sum(ns)))*(sub/0.5)
    
def Mn(arr):
    y = 0
    for X in arr:
        y=y+1
    return y
    
