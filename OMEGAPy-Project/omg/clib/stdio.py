from .cext import *
from io import SEEK_END,SEEK_CUR,SEEK_SET
from msvcrt import *
char = '\0'

def scanf(stack:int):
    _ = achar()
    for i in range(stack):
        _.addchar(getch())
    return _

def strinput():
    getInput = PyInput()
    return getInput
class FILE:
    def __init__(self):
        ...
    def _open(self,path,mod)->int:
        self._path = path
        self._openedobj = open(self._path,mod)
        return 1
    def _fwrite(self,string)->int:
        self._openedobj.write(string)
        return 1
    def _fread(self)->str:
        return self._openedobj.read()
    def _fseek(self,cookie)->int:
        return self._openedobj.seek(cookie)


def fopen(obj:FILE,path,mod):
    obj._open(path,mod)
def fprintf(obj:FILE,*args)->int:
    obj._fwrite(str(format%args)+'\n')
    return 1
def fgets(obj:FILE)->str:
    return obj._fread()
def fread(obj:FILE)->str:
    return obj._fread()+'\n'
def fwrite(obj:FILE,string)->int:
    return obj._fwrite(string)
def fputs(obj:FILE,string)->int:
    return obj._fwrite('\n'+string)
def fseek(obj:FILE,where:int):
    return obj._fseek(where)

def puts(obj)->str:print(obj)

def printf(format:str,*args)->str:
    print(format%args,end='')

def read_char()->char:
    return getch()
