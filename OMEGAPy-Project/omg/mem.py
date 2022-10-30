import ctypes as _c
import tracemalloc as _malloc
import re
import sys
from .tools import listTool
from .tools import strTool
from .error_handling import TypeError,ValueError,SyntaxError,MemoryError


class size_t():
    pass



def sizeof(pyobj:size_t):
    if hasattr(pyobj,'__sizeof__'):
        return pyobj.__sizeof__()
    return sys.getsizeof(pyobj)


class strpointer():
    def __init__(self,Bytes): 
        if type(Bytes) != bytearray:
            raise TypeError ('Invalid Type!')
        self.bytes = Bytes
        self._memview = memoryview(self.bytes)
    def __str__(self):
        list_for = listTool.list_for_each(self._memview,lambda x:chr(int(x)))
        inner = listTool.list_for_inner(list_for)
        translated_to_alist = listTool.ToString(listTool.GAItemlist(inner))
        return translated_to_alist
    def __getitem__(self,item):
        if type(item) == str:
            if item == 'full':
                return self._memview.tobytes().decode()
            return chr(self._memview[int(item)])
        elif type(item) == int:
            return self._memview[item]
        elif type(item) == tuple:
            out = []
            for i in range(len(item)):
                out.append(self.__getitem__(item[i]))
            return out
        elif type(item) == slice:
            return self._memview[item.start:item.stop:item.step]
        else:
            raise TypeError('Invalid Type!')
    def __setitem__(self,itid,hexval):
        self._memview.__setitem__(itid,hexval)
        
        
def by_str(string:str):
    if hasattr(string,'encode'):
        return bytearray(string.encode('utf-8'))
    return bytearray(string)

