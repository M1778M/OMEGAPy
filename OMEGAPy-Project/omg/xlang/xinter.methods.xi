# IsXinterMethod yes
# IsPythonLibrary yes
# HasMain no
# HasCompile no

$PyRun xgen_readlinex
# class ReadLine reads a line simply
from sys import stdin , stdout
!define "ReadlineException" True

PyClass ReadLine:
	PyDef __init__(self):
		self.initialize = True
		self.runner =     "xiv"
		self.input_method = stdin # PyStdin
	PyDef in_line(self,every=1):
		for char in stdin.read(every):
			yield char
	PyDef write(self,string):
		stdout.write(string)
	PyDef read_line(self):
		return stdin.readline()

metavar const simple_read = ReadLine()

# function for work on strings
!define "Py3string" 3
PyDef _py3string(from_string:str):
	return str(from_string)
PyDef _strinstr(from_string:str,string:str):
	return (True)if(from_string in string)else(False)
PyDef _strcmp(from_string:str,string:str):
	return (True)if(from_string==string)else(False)
PyDef _strinlist(from_string:str,from_list:list):
	return (True)if(from_string in from_list)else(False)
PyDef _strloop(from_string:str,func=lambda x:x):
	out = ''
	for i in from_string:out+=func(i)
	return out
PyDef _strlen(from_string:str):
	return len(from_string)
PyClass string_all:
	py3string=_py3string
	strinstr=_strinstr
	strcmp=_strcmp
	strinlist=_strinlist
	strloop=_strloop
	strlen=_strlen

exac: print(type(simple_read),simple_read)
$End xgen_readlinex

$CommentBlock About_xgen_readlinex
XGenReadlinex is a Xinter Methods that is made for some examples that shows how xinter methods actually works
XGenReadlinex.ReadLine is PyClass that made for reading lines simply and shows a example of PyClass uses in xinter
$End About_xgen_readlinex
$Shell test_xinter_windows
set XInterDataValid="False"
python -c "import os;os.system('set XInterDataValid=\"True\"')"
$End test_xinter
$CommentBlock About_test_xinter
DataValid is a simple ShellRunFunction
$End About_test_xinter
