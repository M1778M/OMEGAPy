from .tools import listTool as LT
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
        self.y = y
        self.nus = y
        self.x = x
        if x == 0:
            raise AttributeError('Attribute x cannot be 0')
        self.answer = y**(1/x)
    def ret(self):
        return self.answer
    def __repr__(self):
        return f'{self.answer}'
def sqrt(y,x=2):
    return UnderSquareRoot(y,x).ret()

class K(int):
    def __init__(self, i):
        self.Integer = i
        super(K, self).__init__()
    def __eq__(self,x):
        return self.Integer == x
    def __ne__(self,x):
        return self.Integer != x
    def __repr__(self):
        if self.Integer < 999_999:
            return f"{self.Integer/1_000}K"
        elif self.Integer < 999_999_999:
            return f"{self.Integer/1_000_000}M"
        elif self.Integer < 999_999_999_999:
            return f"{self.Integer/1_000_000_000}B"
        elif self.Integer < 999_999_999_999_999:
            return f"{self.Integer/1_000_000_000_000}T"
        elif self.Integer < 999_999_999_999_999_999:
            return f"{self.Integer/1_000_000_000_000_000}q"
        else:
            return f"{self.Integer/1_000_000_000_000_000}q"       

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
 

def m_(x1,y1)->'y2':
    x2 = 100
    y2 = (y1*x2)/x1
    return y2

def m_p(x1,x2,y1)->'y2':
    y2 = (y1*x2)/x1
    return y2

def fx12y3_00(x1,x2)->'y3':
    y1=x1-x2
    y2=x2/x1
    x3=y1*y2
    y3=(x1**x2)-(y1**y2)+x3
    return y3

