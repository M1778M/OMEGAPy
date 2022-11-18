#--------------------------------------------------------------
# XINTER_VERSION         : 0.1.1
# XINTER_IPR             : PYTHON_3
# XINTER_HYPER_ZERO      : YES
# XINTER_READABLE_SYNTAX : YES
# XINTER_MACHINE_CODE    : YES
# XINTER_COMPILE_ABLE    : YES
# XINTER_HIGH_LEVEL      : NO
# XINTER_FILE_MANAGER    : PY_FILE_STDIN_STDOUT
# XINTER_XLIB_SUPPORT    : YES
# XINTER_MEMORY_MANAGER  : XLIB
# XINTER_WINDOWS         : YES
# XINTER_LINUX           : IN_BUILD
# XINTER_OPEN_SOURCE     : YES
# XINTER_LEXER           : YES
# XINTER_TYPE_DECLARE    : YES
#---------------------------------------------------------------
#---------------------------------------------------------------
# XINTER_IMPORTS
#import xlib
from clib.cext import define,ifndef,ifdef
from clib import cext
from xbase import MetaVar,MetaMethod,OpenFile
from argparse import ArgumentParser,FileType
from msvcrt import getch,putch
# XINTER_SYSTEM_VARIABLES
parser = ArgumentParser(
                    prog = 'XInterPython',
                    description = 'XInter is a interpreter for xlang',
                    epilog = 'XInter XLang Interpreter and Compiler mod')
# XINTER_DEFINES
ifndef('XINTER_VERSION').define("XINTER_VERSION",'0.1.1')
ifndef('XINTER_RUN').define("XINTER_RUN",None)
ifndef('XINTER_TYPES_VERSION').define("XINTER_TYPES_VERSION",1.0)
ifndef('XINTER_FUNCTIONS_VERSION').define("XINTER_FUNCTIONS_VERSION",1.0)
# XINTER_METAVARS
XINT        = MetaVar('INTEGER',    True)
XFLOAT      = MetaVar('FLOAT',      True)
OPLUS       = MetaVar('PLUS',       True)
OMIN        = MetaVar('MIN',        True)
OMUL        = MetaVar('MUL',        True)
ODIV        = MetaVar('DIV',        True)
UXLPAR      = MetaVar('LPAREN',     True)
UXRPAR      = MetaVar('RPAREN',     True)
XDIGITS     = MetaVar('0987654321', True)
# XINTER_SUBMETHODS
# XINTER_SUBMETHOD_XINTERERROR
class XIE:
    def __init__(self, start_pos, end_pos, error_type, msg):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.error_type = error_type
        self.msg = msg
    
    def format(self):
        result  = f'{self.error_type}: {self.msg}\n'
        result += f'File {self.start_pos.Fn}, line {self.start_pos.Line + 1}'
        return result
# END_XINTER_SUBMETHOD_XINTERERROR
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# XINTER_SUBMETHOD_XInterHandlerError
class XInterHandlerError(XIE):
    def __init__(self,start_pos,end_pos,msg):
        super().__init__(start_pos,end_pos,"XInterHandlerError",msg)
# END_XINTER_SUBMETHOD_XInterHandlerError
#---------------------------------------------------------------------------------
# XINTER_METHODS

# XINTER_METHODS_POSITION
#   Position->Index,Line,Columnumn,Fn,FSource
class Position(MetaMethod):
    def __init__(self, Index, Line, Column, Fn, FSource):
        super().__init__()
        self.Index = Index
        self.Line = Line
        self.Column = Column
        self.Fn = Fn
        self.FSource = FSource

    def next(self, current_char):
        self.Index += 1
        self.Column += 1

        if current_char == '\n':
            self.Line += 1
            self.Column = 0

        return self

    def copy(self):
        return Position(self.Index, self.Line, self.Column, self.Fn, self.FSource)
# END_XINTER_METHODS_POSITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# XINTER_METHODS_TOKEN
#   Token->Type,Value
class Token(MetaMethod):
    def __init__(self,Type,Value=None):
        super().__init__()
        self.type  = Type
        self.value = Value
    def __repr__(self):
        if self.value is not None:
            return f"{self.type}->{self.value}"
        else:
            return f"{self.type}"
# END_XINTER_METHODS_TOKEN
# ~~~~~~~~~~~~~~~~~~~~~~~~
# XINTER_METHODS_LEXER
#   Lexer->Fn,Source
class Lexer(MetaMethod):
    def __init__(self,Fn,Source):
        super().__init__()
        self.fn = Fn
        self.source = Source
        self.position = Position(-1,0,-1,Fn,Source)
        self.current_char = None
        self.next()
    def next(self):
        self.position.next(self.current_char)
        
        if self.position.Index < len(self.source):
            self.current_char = self.source[self.position.Index]
        else:
            self.current_char = None
    def create_tokens(self):
        tokens=[]
        
        while self.current_char != None:
            if self.current_char in ' \t':
                self.next()
            elif self.current_char in XDIGITS.get():
                tokens.append(self.make_int())
            elif self.current_char == '+':
                tokens.append(Token(OPLUS.get()))
                self.next()
            elif self.current_char == '-':
                tokens.append(Token(OMIN.get()))
                self.next()
            elif self.current_char == '*':
                tokens.append(Token(OMUL.get()))
                self.next()
            elif self.current_char == '/':
                tokens.append(Token(ODIV.get()))
                self.next()
            elif self.current_char == '(':
                tokens.append(Token(UXLPAR.get()))
                self.next()
            elif self.current_char == ')':
                tokens.append(Token(UXRPAR.get()))
                self.next()
            else:
                start_pos = self.position.copy()
                char = self.current_char
                self.next()
                return [], XInterHandlerError(start_pos, self.position, "'" + char + "'")

        return tokens, None
    def make_int(self):
        IntStr = ''
        Dot = 0

        while self.current_char != None and self.current_char in XDIGITS.get() + '.':
            if self.current_char == '.':
                if Dot == 1:
                    break
                Dot += 1
                IntStr += '.'
            else:
                IntStr += self.current_char
            self.next()

        if Dot == 0:
            return Token(XINT.get(), int(IntStr))
        else:
            return Token(XFLOAT.get(), float(IntStr))
# END_XINTER_METHODS_LEXER
#~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------------------------------------------------------------------------
# XINTER_MAIN

def run_line(fn,line):
    out = Lexer(fn,line).create_tokens()
    return out

def inline(fn,lines:str):
    lines = lines.split(';')
    if len(lines) == 1:
        source = lines[0]
    else:
        source = lines
    print(source)
    if type(source) == list:
        out = []
        for line_ in source:
            out.append(run_line(fn,line_))
        return out
    elif type(source) == str:
        return run_line(fn,source)
    else:
        raise TypeError(f"UnkownType of source -> '{type(source)}'")

def active_interpreter():
    while 1:
        print("XLANG/XInter~# ",end='')
        Input = input()
        if Input == '\r' or Input == '\n':
            continue
        out = (inline('<stdin>',Input))
        if out[1] == None:
            print(out)
        elif out[1] != None:
            print(out[1].format())
        
def filerun(fn,source:str):
    Source = source.split('\n')
    for line in Source:
        out = inline(fn,line)
        if out[1] == None:
            print(out)
        elif out[1] != None:
            print(out[1].format())
def main():
    parser.add_argument('filename',dest="file"
        ,help="filename of a program that wrote in xlang."
        ,type=FileType('r'),required=False)
    parser.add_argument('-i','--interpreter',dest="interpreter"
        ,help="enters in an interpreter for coding(xlang)."
        ,action='store_true',required=False)
    args = parser.parse_args()
    
    if args.file:
        filerun(args.file,OpenFile(args.file))
    elif args.interpreter:
        active_interpreter()
    else:
        print("Error in inputs please use --help")
        exit()

    