import ctypes
import os,sys
import pickle

class SystemData():
    def __init__(self):
        self.data = {}
    def save(self):
        with open('sysdt.pack','wb') as f:
            pickle.dump(self.data,f)
            f.close()
        return True
    def open(self):
        if 'sysdt.pack' in os.listdir():
            with open('sysdt.pack','rb') as f:
                self.data = pickle.load(f)
                f.close()
            return True
        else:
            self.save()
            self.open()
    def return_data(self):
        return data
    def delete(self,dataName:str):
        del self.data[dataName]
        return True
    def add(self,dataName:str,value):
        self.data[dataName] = value
        return True

_system_data_manager = SystemData()

class SystemExceptionError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def str2ccharp(Str:str):
    return ctypes.c_char_p(bytes(Str.encode('utf-8')))


def raise_(err:Exception,msg:str):
    raise err(msg)

def run_cmd(command : ctypes.c_char_p = ctypes.c_char_p(b'')):
    try:
        out = os.system(command.value.decode())
        return out
    except Exception as err:
        raise_(SystemExceptionError,err)



