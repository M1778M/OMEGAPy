from compile_options import TellaCompiler

LAST_FILE_COMPILED = None
tella = TellaCompiler()

def _CompileByExecute(code:str):
    tella.execute (code)
def _CompileByFilepath(filepath:str):
    LAST_FILE_COMPILED = tella.fexecute(filepath)

class OMEGAPyCompilePy:
    def __init__(self):
        self.version       = 0.1
        self.static_method = "ccpy"
        self.all_methods   = ['ccpy','cfp']
    def method_checker (self,method):
        if method in self.all_methods:
            return True
        return False
    def _ccpy (self,code:str):
        _CompileByExecute (code)
    def _cfp(self,filepath:str):
        _CompileByFilepath(filepath)
    def _compile(self,method,source):
        if not self.method_checker (method):return False
        if method == 'ccpy':
            self._ccpy(source)
        elif method == 'cfp':
            self._cfp(source)
        else:
            return False
    def compile(self,source):
        return self._compile(self.static_method,source)
