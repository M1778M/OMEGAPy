from . import etu
from .error_handling import UnknownError,ConnectionFaildError,ValueError
import hashlib as _hl
import time as _time
import random as _random

def random_secure_str(x):
    al = 'zxcvbnmasdfghjklqwertyuiop'
    txt = al+'1234567890_-+=~`"\'.><?/\\[]{}@#$%^&*()!|\t'+al.upper()
    _random.seed (_time.time())
    randstr = ''
    for i in range(x):
        index = _random.randint (0,len(txt)-1)
        randstr += txt[index]
    return randstr

def _StdConMethod (secret):
    flag = 'StdC322'
    return _hl.sha256(str(random_secure_str(1024-len(flag))).encode() ).hexdigest()

def _SecureConMethod (secret):
    encd = _hl.sha256 (str(secret+random_secure_str(256)).encode())
    return encd.hexdigest()
    
def _QuickConMethod (secret):return _StdConMethod(secret)

class methods:
    secure_connection   = 'securecon'
    standard_connection = 'stdcon'
    quick_connection    = 'quickcon'

def get_method_byname (method):
    if method == 'stdcon':
        return _StdConMethod
    elif method == 'securecon':
        return _SecureConMethod
    elif method == 'quickcon':
        return _QuickConMethod
    else:
        raise ValueError (f"Cannot Find method '{method}'")

def seccheck (secret):
    if len (secret) <= 8:
        return True
    else:
        return False

class Signer :
    methods = ['stdcon','securecon','quickcon']
    def __init__(self,method:str,secret:str):
        self.error = False if seccheck (secret)==False else True
        self.__secret = secret
        self.method = get_method_byname (method)
    def make_signer (self):
        if self.error:
            raise UnknownError('')
        self.__sign_key = self.method(self.__secret)
        return True
    def check_sign (self,sign):
        if self.__sign_key == sign:
            return True
        return False
    def _echeck(self):
        return True if self.error else False
    
def SignMethodMaker (method='stdcon',secret:str=random_secure_str(16)):
    return Signer (method,secret)
    
