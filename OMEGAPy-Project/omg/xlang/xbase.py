from .clib import cext
from .clib.cext import *
from .clib import *
from .xlib import *
from . import *
from threading import Thread
global MetaVar
global xexec
def _split_line_by_space(line):
    return line.split(' ')
_slbs = _split_line_by_space

def clean_sp(x):
    return x.strip(' ')
def _mt(line,flag=False):
    line_split = line.split('=')
    name=''
    var =''
    for i in line_split[0]:
        if i!=' ':
            name+=i
    for i in line_split[1]:
        if i!=' ':
            var+=i
    return f"{name} = MetaVar({var},{flag})"
def _ifin(x,y):
    return x in y
def _e(x,y):
    return x==y
def _fix(line,rep):
    for i in rep:
        line = line.replace(i,rep[i])
    return line
def _lin(x,y):
    for i in x:
        if i in y:
            return True
    return False

def is_true(ms,ew):
    if ms in ew:
        return ms
    else:
        raise SyntaxError
def _where(x,y):
    if x in y:
        for i in range(len(y)):
            if x == y[i]:
                return i
    else:
        return False
def _wherein(x,y):
    for i in range(len(y)):
        if x in y[i]:
            return i
    return False
def _funcssyntax(line):
    line_split = line.split(' ')
    out = ''
    out+= line_split[0].strip('!')+'('
    del line_split[0]
    for i in line_split:
        if i==line_split[-1]:
            out+=i
        else:out+=i+','
    out+=')'
    return out
def safe_clean_sp(line):
    out = ''
    x=0
    for i in line:
        if i!=' ' or i!='\t' and x==1:
            x = 1
            out+=i
        elif i==' ' or i=='\t' and x==1:
            continue
    return out
def is_clean(line):
    if line == '' or line == '\t' or line.isspace():
        return False
    return True
class CompileError(Exception):
    def __init__(self,msg=''):
        super().__init__(msg)

class xi:
    def __init__(self):
        self.initialize = {}
        self.base_varchar = '#'
        self.base_vars_cnd = ['IsXinterMethod','IsPythonLibrary','HasMain','HasCompile']
        self.kw_varchar = '$'
        self.keywords = ['PyRun','CommentBlock','Shell','End']
        self.pyrun_key_words = ['PyClass','PyDef','Pysizeof']
        self.pyrun_key_words_rep = {'PyClass':'class','PyDef':'def','Pysizeof':'sizeof'}
        self.pyrun_algkeys = ['metavar','exac']
        self.pyrun_runfunc = '!'
        self._comments = []
        self.ShellRun = 'normal'
        self._xireadf = 0
        self._xireadtemp = ''
    def __call__(self,source):
        return self.xicompile(source)
    def xiread(self,source):
        ret = {}
        for line in source.split('\n'):
            line_split = _slbs(line)
            if not is_clean(line):
                continue
            if self._xireadf == 1:
                if line_split[0] == '$End':
                    if line_split[1] == self._xireadn:
                        ret[self._xireadn] = {'type':self._xireadt,'name':self._xireadn,'source':self._xireadtemp}
                        self._xireadtemp = ''
                        self._xireadf = 0
                        self._xireadt = ''
                        self._xireadn=''
                        continue
                    else:
                        continue
                else:
                    self._xireadtemp+=line+'\n'
                    continue

            if self._xireadf!=1 and _e(line_split[0],self.base_varchar):
                if _ifin(line_split[1],self.base_vars_cnd):
                    self.initialize[line_split[1]] = is_true(line_split[2].lower(),['no','yes'])
                else:
                    raise SyntaxError
            
            elif _e(line_split[0][0],self.kw_varchar):
                if _ifin(line_split[0].strip('$'),self.keywords):
                    Name = line_split[1]
                    self._xireadn = Name
                    self._xireadf=1
                    self._xireadt=self.keywords[_where(line_split[0].strip('$'),self.keywords)]
                else:
                    raise SyntaxError
            else:
                if self._xireadf==1:
                    continue
                else:
                    raise SyntaxError
        
        return ret
    def xisyntax(self,source:dict):
        name=source['name']
        type_=source['type']
        source=source['source']
        out = ''
        if _ifin(type_,['PyRun','Shell']):
            if type_=='PyRun':
                for line in source.split('\n'):
                    line_split = _slbs(line)
                    if not is_clean(line):
                        continue
                    if line[0] == '#':
                        continue
                    if _ifin('!',line):
                        w = _wherein('!',line_split)
                        s_ = line_split[w]
                        if len(line_split)==3 and _e(line[0],'!'):
                            out+=_funcssyntax(line)+'\n'
                            continue
                        elif s_[0] == '!':
                            out+=_funcssyntax(line)+'\n'
                            continue
                        else:
                            raise SyntaxError
                    if _lin(self.pyrun_key_words,line):
                        for i in self.pyrun_key_words:
                            if i+' ' in line:
                                line = _fix(line,self.pyrun_key_words_rep)
                        out+=line+'\n'
                        continue
                    if _lin(self.pyrun_algkeys,line):
                        if self.pyrun_algkeys[0] in line:
                            if line_split[0] == self.pyrun_algkeys[0] and line_split[1] == 'const' and _ifin('=',line):
                                line = line[line.find('const')+6:]
                                line = _mt(line,True)
                                out+=line+'\n'
                                continue
                            elif line_split[0] == self.pyrun_algkeys[0] and _ifin('=',line):
                                line = line[line.find('metavar')+8:]
                                line = _mt(line,False)
                                out+=line+'\n'
                                continue
                        elif self.pyrun_algkeys[1] in line:
                            if 'exac' in line_split[0] and _ifin(':',line_split[0]):
                                line = line[line.find(':')+1:]
                                for i in range(len(line)):
                                    line = safe_clean_sp(line)
                                out+=line+'\n'
                                continue
                    else:
                        out+=line+'\n'
                                
                return out
            elif type_=='Shell':
                return source
            else:
                raise ValueError('Invalid Type.')

        else:
            raise SyntaxError
    def _execute(self,code):
        xexec(code)
        return True
    def _shellexecute(self,code):
        from subprocess import getoutput
        out = ''
        for i in code.split('\n'):
            out+=getoutput(i)
        return out
    def xicompile(self,source):
        config = self.xiread(source)
        for Item in config:
            if config[Item]['type'] == 'PyRun':
                syntax = self.xisyntax(config[Item])
                self._execute(syntax)
            elif config[Item]['type'] == 'Shell':
                syntax = self.xisyntax(config[Item])
                if self.ShellRun == 'normal':
                    print(self._shellexecute(syntax))
                else:
                    Thread(target=self._shellexecute,args=(syntax,)).start()
            elif config[Item]['type'] == 'CommentBlock':
                self._comments.append(config[Item]['source'])
            else:
                raise CompileError('Invalid Block.')
        return 1
Xi=xi()


# Method

class MetaVar:
    def __init__(self,value,const=False):
        self.__value = value
        self.__is_const = const
    def change_value(self,newValue):
        if self.__is_const != True:
            self.__value = newValue
            return 1
        else:
            return None
    def __repr__(self):
        if self.__is_const:
            return f'<object Const_MetaVar> <Value \'{self.__value}\'>'
        return f"<object MetaVar> <Value \'{self.__value}\'>"
    def __call__(self):
        return self.__value
    def get(self):
        return self.__value


class MetaMethod:
    def __init__(self):
        self.__META_METHOD = True
    def _IsMetaMethod(self):
        return self.__META_METHOD

def OpenFile(filepath:str):
    Source = ""
    with open(filepath,'r')as file:
        Source = file.read()
        file.close()
    return Source

def xexec(code):
    exec(code,globals())
