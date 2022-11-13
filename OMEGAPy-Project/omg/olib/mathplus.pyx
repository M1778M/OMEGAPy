from .fastbit import N,W,Z,Q,Qp,pi,UnderSquareRoot,usqrt
from . import fastbit




def sqrt(y,x=2):
    if y+1 == y+1 and x!=0:
        return y**(1/x)
    else:
        raise TypeError()

def add(x,y,f=3):
    z = str(float((float(x)+float(y))))
    try:
    z_ = z.split('.')[1]
    _z = z.split('.')[0]
    except:
        raise ValueError('The "add" function just supports 16BIT_INTEGER_FLOAT')
    if (len(z_) <= f):
        return x+y
    else:
        return float(_z+'.'+z_[:f])
def addp(*args,f=3):
    z = float()
    for i in args:
        add(z,i,f)
    return z

