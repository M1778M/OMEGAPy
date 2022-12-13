from ctypes import *
from subprocess import Popen

def _ExecuteSource(code:str):
    exec(code,globals())

TokenSecurity = 'NotSecure'
Tokens = ['ZarmanIDE']

class _TOKEN_CHECKER:
    def __init__(self,token:str):
        if Submit_Token(token):
            self.trusted_method = True
        else:
            self.trusted_method = False

def Submit_Token(token):
    if token in Tokens:
        return True
    return False

class TellaCompiler ():
    def __init__(self):
        self.version = 1.
        self.token = 'ZarmanIDE'
        self.checker = _TOKEN_CHECKER(self.token)
    def execute(self,code:str):
        if self.checker.trusted_method:
            _ExecuteSource (code)
    def fexecute(self,filepath:str,args=[]):
        return Popen (['python',filepath]+args)

