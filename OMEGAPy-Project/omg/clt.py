# CommandLineTool
from .tools import listTool
from .xlang import xinter,xbase,methods

readline=methods.ReadLine()

_compiler = xbase.xi()
_cltsyn = xbase.Syntax.from_dict({'Write':'stdout.write','Read':'stdin.read','ReadLine':'stdin.readline'})
xinter.press_syntax(_cltsyn,_compiler)

code = \
"""
# SoruceIsClt yes
# SourceIsValid yes
# SourceWillCompile yes
$PyRun clt_module


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

_compiler(code)
