# CommandLineTool
from .tools import listTool as _listTool
from .xlang import xinter as _xinter,xbase as _xbase,methods as _methods

readline=_methods.ReadLine()

_compiler = _xbase.xi()
_cltsyn = _xbase.Syntax.from_dict({'Write':'stdout.write','Read':'stdin.read','ReadLine':'stdin.readline'})
_xinter.press_syntax(_cltsyn._syndict,_compiler)

code = \
"""
# HasCompile yes
# IsOmgLibrary yes
# HasMain no

$PyRun clt_module
import time
from colorama import init as _init,Fore,Back
from threading import Thread
PyDef sprint(*args,fc='',bc=''):
    for arg in args:
        print(str(fc)+str(bc)+str(arg),end='')
PyDef reset(w=2):
    if w == 2: print(end=f'{Fore.RESET}{Back.RESET}')
    if w == 1: print(end=f'{Fore.RESET}')
    if w == 0: print(end=f'{Back.RESET}')
global _flag
_flag = 0
PyDef waiting_flag():
    global flag
    flag=1

PyDef Waiting ( func : type(reset) , args=(waiting_flag,) ):
    global _flag
    if _flag == 1:
        _flag=0
    prx = Thread(target=func , args=args)
    prx.run()
    while True:
        if _flag == 1:
            return True
        sprint("Waiting...\\r")
        time.sleep(0.5)


$End clt_module
$CommentBlock clt_comment
Clt Base is written in Xlang
Clt is an opensource command line tool for doing command line operations like read and write and handle it easy and fast
Clt uses "OMEGAPy-CommandLine-Algorithm" for having better focus
Clt is a module used in  "easy to use" or etu for giving some operations for user that uses etu

Clt Syntax:
    Clt has a very easy syntax and the main syntax of it its python syntax but with some changes line new keywords like Write and Read and ReadLine

$End clt_comment
"""

_rdsyn=_compiler.xiread(code)
_rdsyn=_rdsyn['clt_module']
_gsyn = _compiler.xisyntax(_rdsyn)
_compiler._execute(_gsyn)
from .xlang.xbase import sprint,Waiting,waiting_flag,_flag,reset
