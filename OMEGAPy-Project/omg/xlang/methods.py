from pathlib import Path 
from .xbase import Xi,OpenFile
from . import xbase
Xi(OpenFile(str(Path(__file__).absolute().parent)+'/xinter.methods.xi'))
ReadLine=xbase.ReadLine
string_all=xbase.string_all
