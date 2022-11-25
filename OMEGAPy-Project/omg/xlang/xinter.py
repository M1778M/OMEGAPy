#--------------------------------------------------------------
# XINTER_VERSION         : 0.1.1
# XINTER_IPR             : PYTHON_3
# XINTER_READABLE_SYNTAX : YES
# XINTER_FILE_MANAGER    : PY3_FILE_STDIN_STDOUT
# XINTER_XLIB_SUPPORT    : YES
# XINTER_MEMORY_MANAGER  : XLIB
# XINTER_WINDOWS         : YES
# XINTER_LINUX           : 90%
# XINTER_OPEN_SOURCE     : YES
# XINTER_TYPE_DECLARE    : YES
#---------------------------------------------------------------
#---------------------------------------------------------------
# XINTER_IMPORTS
#import xlib
from .clib.cext import define,ifndef,ifdef
from .clib import cext
from .xbase import MetaVar,MetaMethod,OpenFile,xi,Xi,Syntax,_imp
from . import methods,xbase as _base
# XINTER_SYSTEM_VARIABLES
# XINTER_DEFINES
ifndef('XINTER_VERSION')          .define("XINTER_VERSION",'0.1.1')
ifndef('XINTER_RUN')              .define("XINTER_RUN",None)
ifndef('XINTER_TYPES_VERSION')    .define("XINTER_TYPES_VERSION",1.0)
ifndef('XINTER_FUNCTIONS_VERSION').define("XINTER_FUNCTIONS_VERSION",1.0)
# XINTER_METAVARS
XInterVersion           = MetaVar("0.1",True)
XInterReadLine          = MetaVar("methods.ReadLine",True)
XInterXiVersion         = MetaVar('0.5.1',True)
XInterXiCompilerVersion = MetaVar('0.2.2',True)
XInterXiSyntaxVersion   = MetaVar('0.2.2',True)
XInterMToken            = MetaVar('XInterX',True)
# XINTER_SYNTAXS
standardsyn = Syntax.from_dict({"PyFrom":"from","PyImport":"import","PySet":"set","PyList":"list","PyInt":"int","PyStr":"str","PyType":"type","PyComplex":"complex","PyFloat":"float"})
standardsyn._tokenize(XInterMToken.get())
# XIMPORTS
ReadLine=_base.ReadLine
_string_all=_base.string_all
# XINTER_FUNCTIONS
def run_file(path): return Xi(OpenFile(path))

def run_str(code): return Xi(code)

def import_module(module):_imp(module)

def press_syntax(syntax:dict,compiler:xi):
    for item in list(syntax):
        compiler.pyrun_key_words_rep[item]=syntax[item]
# END_XINTER
