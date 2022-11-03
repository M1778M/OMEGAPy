############  Public Modules

try:
    from cython import cfunc,cclass,int as c_int
    from colorama import init,Fore,Back
    from numpy import array
    from typing import Any
    import pathlib as pl
    import numpy as np
    import cython
    import sys
    import re
    import os
except ImportError as err:
    raise ImportError (err)
except Exception as err:
    raise EtuExceptionError(err)
###############################################################################################
###############################################################################################


############  OMEGAPy Modules

try:
    from . import __need__ as stdn
    from .error_handling import *
    from .tools import listTool
    from .algoritm import Xalg
except:
    try:
        from . import __need__
        stdn = __need__
    except ImportError as err:
        raise ImportError (err)
    except Exception as err:
        raise EtuExceptionError(err)
###############################################################################################
#-------------------------------------- Etu Globals ------------------------------------------

###############################################################################################
#-------------------------------------- Etu BaseMethods ---------------------------------------
class _ETU_COMMENT:
    def __init__(self,comment):
        pass
    def __new__(self,comment):
        return '#'+str(comment)

class Var:
    def __init__(self,value):
        self._defineVal = value
    def __new__(self,value):
        self._defineVal = value
        return value
def _getalgoritm():
    ...
class _ETU_MULTY_COMMENT:
    def __init__(self,*comments):
        pass
    def __new__(self,*comments):
        commenteds = []
        for comment in comments:
            commenteds.append("#"+str(comment))
        return commenteds
###############################################################################################
#----------------------------------------- Etu Basics ----------------------------------------
_ETU_CONNECTIONS = _ETU_COMMENT("Python3Api")
_ETU_LICENSE = _ETU_COMMENT("OMEGAPy-NoneSpaceSTDOpenLicense")
_ETU_VERSION = Var(.02)
_ETU_ALGORITHM = Var("By OMEGAPy_ETUx_WindowsBased32")
_ETU_SYNTAX = Var("By Python3-NoneSpaceSyntax")
_ETU_STANDARD_MODULES = _ETU_MULTY_COMMENT('stdn','cython','sys','re','os','numpy','pathlib','colorama','error_handling','typing','tools')
_ETU_MEMORY_MANAGEMENT = _ETU_COMMENT("By Python3")
ETU_BASE = Var((dir(),_ETU_COMMENT("EasyToUse Standard Module")))
###############################################################################################


class EtuExceptionError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

init()


def nothing():pass


class Condition():
    def __init__(self,conditionStr:str):
        self.cs = conditionStr
    def _check(self):
        return self.cs

@cclass
class c_for():
    def std_print(i):
        print(i)
    def __init__(self,i:c_int,condition:Condition,job:str,work:type(nothing)):
        self.i = i
        self.cnd = condition
        self.job = job
        self.work = work
        self._do_while()
    def _do_while(self):
        flag = True
        i = self.i
        while flag:
            if not eval(self.cnd._check()):
                flag = False
                break
            i += self._takejob(self.job)
            
            self.work(i)
    def _takejob(self,job):
        int_a = 0
        for i in range(len(job)):
            if job[i]=='+':
                int_a+=1
            elif job[i]=='-':
                int_a-=1
            elif job[i]=='*':
                int_a*=int(job[i+1])
            elif job[i]=='/':
                int_a/=int(job[i+1])
            elif job[i]=='**':
                int_a**=int(job[i+1])
            elif job[i]=='//':
                int_a//=int(job[i+1])
            elif job[i]=='%':
                int_a%=int(job[i+1])
            else:
                pass
        return int(int_a)

class Fail(Warning):
    def __init__(self,msg):
        super().__init__(msg)
    

@cclass
#------------------------------ PyObject
class PyObject(object):
    def __init__(self,*args):
        super().__init__()
        self._args=args
        self.__save_range = []
    def run_with_compile(self,function_,send_args=True):
        compiledObject = cython.compile(function_)
        if send_args:
            thread = stdn.threading.Thread(target=compiledObject,args=self._args)
            thread.start()
        else:
            thread = stdn.threading.Thread(target=compiledObject,args=tuple())
            thread.start()
    def cdef(self,func,name):
        compiledObject = cython.compile(func)
        
        return setattr(self,name,compiledObject)
    def sizeof(self,obj):
        x = sys.getsizeof(obj)
        return x
    def declare(self,name,type_,value):
        try:
            setattr(self,name,type_(value))
        except:
            raise UnknownError("Unknown Error process Id -> [%s]" % os.getpid())
    def add_newtype(self,class_):
        super(class_).__init__()
    def execute_code_on_defined_object(self,code,definedn,byname:str='DefinedObj'):
        exec(f"{byname} = {self.__save_range[definedn]}",globals())
        exec(code)
    def save_databy(self,format='python',filepath='./.saved_PyObject_data'):
        if format == 'python':
            with open(filepath,'w')as(f):
                f.write(f'PyObjectFormatedByList = {self.__save_range}')
                f.close()
            return True
        else:
            raise CoreError ("Format IsNotValid.")
    def read_databy(self,format='python',filepath='./.saved_PyObject_data'):
        if format == 'python':
            with open(filepath,'r')as(f):
                exec(f.read(),globals())
                f.close()
            self.__save_range = PyObjectFormatedByList
            return PyObjectFormatedByList
        else:
            raise CoreError ("Format IsNotValid.")
    def define(self,obj):
        if type(obj)==type:
            raise TypeError ("Cannot define type like.")
        def randomName():
            return ('defineObj'+str(stdn.random.randint(9999999,99999999)))
        self.declare('defObj'+((str(obj))if hasattr(obj,'__str__')else(randomName())),type(obj),obj)
        self.__save_range.append(obj)
    def deflist(self):
        return self.__save_range
PyObject = cython.typedef(PyObject)
#---------------------------------

class CoreException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class NoneSpaceSyntaxError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def fprint(*args,formatEncode='utf-8',cs:Fore=None,ce=Fore.RESET,e='\n'):
    op = ""
    if cs:
        for item in args:
            print(cs+item+ce,end='')
            op += str(item)
    else:
        for item in args:
            print(item,end='')
            op += str(item)
    print(e,end=e)
    return op.encode(formatEncode)

class private:
    def __init__(self,valOobj:Any):
        self.___ = lambda :valOobj
    def __call__(self):
        return self.___()

class public:
    def __init__(self,valOobj:Any):
        self._ = valOobj
    def __call__(self):
        return self._
    
@cfunc
def gtime(appn:str):
    from os import system
    from time import time
    def log(LOG):
        print(LOG)
    gt = time()
    system(appn)
    get = time()
    log("Start Time %s" % str(gt))
    log("End Time %s" % str(get))
    log("\nTotal : %s" % str(get-gt))
    return get-gt

def stdconvert(_2type,val): return ((_2type)(val));
def qconvert(_2type,val):
    try: return stdconvert(_2type,val);
    except: return None;

@cclass
class function():
    options = ['name:str','args=[]','variables={}','lines=[]','function(name="Example",args=["Name"],variables={"GetName":"Name"},lines=["print(GetName)"])']
        
    def __init__(self,name:str,args=[],variables={},lines=['pass']):
        self.name = name
        self.args = args
        self.vars = variables
        self.lines = lines
    def run(self,args=()):
        runned = stdn.threading.Thread(target=self.exe(),args=args)
        runned.start()
    def ___make(self):
        out = 'def '
        print('Start Making...')
        defName = 'def {}(): pass'
        defArgs = 'def {}({}): pass'
        defVar = '{} = {}'
        defLine = 'def {}({}):'
        nx = '\n\t'
        defArgs_t = ''
        try:
            for i in self.name:
                if ' ' in self.name:
                    self.name.strip(' ')
            try:
                exec(f'{defName.format(self.name)}')
            except Exception as err:
                raise NoneSpaceSyntaxError (err)
            for i in self.args:
                defArgs_t += f'{i},'
            try:
                exec(defArgs.format(self.name,defArgs_t))
            except Exception as err:
                raise NoneSpaceSyntaxError (err)
            formating = defLine.format(self.name,defArgs_t) + nx
            for i in self.vars:
                if type(i) is not str:
                    raise IReturnValueError (f'Value Invalid Type Of VariableName {i} In {self.vars}\nCan\'t Set Variable In Program')
                if ' ' in i:
                    raise NoneSpaceSyntaxError (f'Invalid Syntax Of VariableName {i}.')
                
                formating += defVar.format(i,self.vars[i]) + nx
                try:
                    exec(formating)
                except Exception as err:
                    raise NoneSpaceSyntaxError (err)
            defLine = defLine.format(self.name,defArgs_t)
            for i in self.vars:
                defLine += nx + defVar.format(i,self.vars[i])
            defLine += nx
            copy = defLine
            if len(self.vars) == 0:
                defLine += 'pass'
            try:
                exec(defLine)
            except Exception as err:
                raise NoneSpaceSyntaxError (err)
            defLine = copy
            for i in self.lines:
                defLine += i + nx
            try:
                exec(defLine)
            except Exception as err:
                raise NoneSpaceSyntaxError (err)
                
        except Exception as err:
            print('Warning: CVS-ERROR')
        main = 'def {}({}):'
        
        for i in self.vars:
            main += nx + defVar.format(i,self.vars[i])
        main += nx
        
        for i in self.lines:
            main += i + nx
        main = main.format(self.name,defArgs_t)
            
        return main
    def exe(self):
        exec(self.___make(),globals())
        exec(f"_function__NoneSpaceGlob = {self.name}",globals())
        return __NoneSpaceGlob
    def __repr__(self):
        return self.___make()

def _tnow():
    from datetime import datetime
    import time
    def now():
        return str(datetime.now())
    return now()

    
class Edit():
    def __init__(self,file:str):
        if not(pl.Path(file).is_file()):
            raise FileNotFoundError(f'Cannot find {file}')
        self._file = file
    def clear(self):
        with open(self._file,'w')as(f):
            f.write('');f.close()
    def write(self,text:str,overwrite=False,is_line=True):
        with open(self._file,('a') if not overwrite else 'w')as(f):
            (f.write(text))if not(is_line)else(f.writelines([text]));f.close()
        return True
    def read(self,linen:int=None):
        if(linen):
            with open(self._file,'r')as(f):
                f.seek(linen);line = f.readline();f.close();return line
        else:
            with open(self._file,'r')as(f):
                f.seek(0);lines = f.read();f.close();return lines
        
class UnknownError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class belog_cl():pass

def __belog_Excute_Colors():
    execute_code = '{}.{}'
    fr = dir(Fore)
    bk = dir(Back)
    lfrn = []
    lbkn = []
    belog_cl.colors = []
    belog_cl.bcolors = []
    for i in fr:
        if i[0] == '_':
            pass
        else:
            lfrn.append(i)
    for i in bk:
        if i[0] == '_':
            pass
        else:
            lbkn.append(i)
    for i in lfrn:
        exec(f"belog_cl.colors.append({execute_code.format('Fore',i)})")
    for i in lbkn:
        exec(f"belog_cl.bcolors.append({execute_code.format('Back',i)})")
    return True
__belog_Excute_Colors()

class InvalidMODError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class InvalidPrinterArgumentError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        
        




class qshell():
    def __init__(self):
        import win32console
        self.con = win32console
        self.__log = set()
    def Test_rightpointer(self):
        sell = qshell()
        print(Fore.CYAN)
        print(sell.right_pointer(4,8,20,7,[f'{Back.RESET}\t(object at {stdn.random.randint(9999,99999)})']*20,from_s_tt=Back.RED,end_point=Back.RESET+'(object ended at here)',inline='~',nextl='  '));
        print(Fore.RESET)
    def Test_method(self):
        myl = ["Windows","Linux","MacOs"]
        self.ask(myl,title="What Is You'r Favorite os?",e="Choose one os:")
        cmd = self.set_method()
        print(f"Input Of set_method Is:[{cmd}] Type:[{type(cmd)}]")
        fprint(f"Oh Nice os [{myl[int(cmd)]}]",cs=Fore.BLUE)
    def Test_KEvent(self):
        myl = ["Windows","Linux","MacOs"]
        self.ask(myl,title="What Is You'r Favorite os?",e="Choose one os:")
        cmd = self.set_method('KEYEVENT')
        sys.stdout.write(cmd+'\n')
        print(f"Input Of set_method Is:[{cmd}] Type:[{type(cmd)}]")
        fprint(f"Oh Nice os [{myl[int(cmd)]}]",cs=Fore.BLUE)
    def set_method(self,methodt='GET'):
        if methodt.upper() == 'GET':
            cmd = input()
            return cmd
        elif methodt.upper() == 'KEYEVENT':
            event = stdn.keyboard.read_key()
            return event
        else:
            error = eprint("class","shellini","InvalidType","Type Of Argument[methodt] In Function self.set_method Is Invalid!")
            self.__log.add(list(error))
    def clear(self):
        from os import system
        from platform import platform
        platform = platform().upper()
        if "LINUX" in platform or "MAC" in platform:
            system('clear')
        elif "WINDOWS" in platform:
            system('cls')
        else:
            eprint("class/function",'shellini/clear','InvalidSystemPlatform','Cant Analize Your SystemPlatform!')
    def box(self,linelen:int,lines:list,up:str='-',down:str='-',right:str='|',left:str='|'):
        out = ''
        out += f'{left} {linelen*up} {right}\n'
        for i in range(len(lines)):
            if len(lines[i])-2==linelen:
                out+=f"{left} "+str(lines[i])+f" {right}\n"
            else:
                space_need = 0
                ln = abs(len(lines[i])-linelen)
                if ln%2==0:
                    out+=f'{left} '+(' '*int(ln/2))+lines[i]+(' '*int(ln/2))+f' {right}\n'
                else:
                    out+=f'{left} '+(' '*int(ln/2))+lines[i]+(' '*int(ln/2))+f' {right}\n'
        out+=f'{left} {linelen*down} {right}'
        return out
    def right_pointer(self,from_:int,from_s:int,lines_n:int,to_s:int,everyline_text:list,from_s_text:str='\t(object started at here)',end_point:str='(object ended at here)',from_s_tt:str=' ',inline:str='-',nextl:str='|'):
        out = ''
        for i in range(from_s):
            out +=from_s_tt
        out+='/'
        for i in range(from_):
            out +=inline
        out+=from_s_text+'\n'
        for i in range(lines_n):
            out+=(from_s_tt*from_s)+f'{nextl}{everyline_text[i]}\n'
        out+=(from_s_tt*from_s)+'\\'+(inline*to_s)+'>'+end_point
        return out
        
    def ask(self,args:list,title="Choose One",titlec=Fore.YELLOW,typE='n',c=Fore.GREEN,e=':',ec=Fore.RED,ae='\n'):
        if typE == 'n':
            fprint(title,cs=titlec)
            for i in range(len(args)):
                fprint(f"[{i}]{args[i]}",cs=c)
            print(ae,end='')
            fprint(e,cs=ec,e='')
        else:
            error = eprint("class","shellini","InvalidType","Type Of Arguement[typE] In Function self.fprint Is Invalid!")
            self.__log.add(list(error))


def sl(obj,**kwargs):
    for k in kwargs.keys():
        if k == 'item_rev':
            try:
                out = reversed(out)
            except:
                out = reversed(obj)
        elif k == 'callby':
            try:
                out = k['callby'](out)
            except:
                out = k['callby'](obj)
        elif k == 'castby':
            try:
                out = ((k['castby'])(out))
            except:
                out = ((k['castby'])(obj))
        elif k == 'check_by':
            try:
                out = (True)if(k['check_by']==out)else(False)
            except:
                out = (True)if(k['check_by']==obj)else(False)
        elif k == 'noncheck_by':
            try:
                out = (True)if(k['check_by']!=out)else(False)
            except:
                out = (True)if(k['check_by']!=obj)else(False)
        else:
            continue
    try:
        methods = dir(out)
        for method in methods:
            if re.match('^__\w+__$',method):
                nname = method.strip('_')
                setattr(out,nname,getattr(out,method))
            else:
                continue
        return out
    except NameError:
        methods = dir(obj)
        for method in methods:
            if re.match('^__\w+__$',method):
                nname = method.strip('_')
                try:
                    setattr(obj,nname,getattr(obj,method))
                except:
                    continue
            else:
                continue
        return obj
    except Exception as err:
        raise Exception(err)


class _Base_ForEach:
    def __init__(self,loop):
        self._loop = loop
        self._inloop = 0
    def nt(self):
        return self._loop[self._inloop+1]
    def bk(self):
        return self._loop[self._inloop-1]
    def seek(self,offset):
        self._inloop = offset
    def getLast(self,append=True):
        if append:
            self._inloop += 1
            return self._loop[self._inloop-1]
        else:
            return self._loop[self._inloop]
        def __getitem__(self,other):
            return self._loop[other]
    def loopon(self,parse_on:function):
        for item in self._loop:
            yield parse_on(item)
    def do(self,parse_on:function):
        return parse_on(self._loop)

def foreach(obj):
    return _Base_ForEach(obj)

@cclass
class belog():
    BELOG_COLORS = Fore
    BELOG_BGCOLORS = Back
    BELOG_MOD_COMMAND_LINE_PRINT = 1
    BELOG_MOD_FILE_WRITE = 2
    BELOG_PRINT_FORMATS = {"INFO":4,"WARNING":8,"CIRTICAL":16}
    START_FROM_CMDLINE =  {"s_color":BELOG_COLORS.GREEN,"e_color":BELOG_COLORS.RESET,"text":"Belog Set By CommandLine mod."}
    START_FROM_FILEWRITE = {"s_color":BELOG_COLORS.GREEN,"text":"Belog Set By File Writer mod"}
    BLOCKS = {"s_color","e_color","b_color","eb_color","text","method","unicode","e_text","s_text","flush","flushed"}
    _class_correct_value = {"INFO" : Fore.GREEN, "WARNING" : Fore.YELLOW, "CIRTICAL" : Fore.BLUE}
    def __init__(self,mod,log_name:str):
        self.mod = mod
        self.log_name = log_name
        self._link_to_colors = belog_cl.colors
        self._link_to_bcolors = belog_cl.bcolors
        if self.mod == self.BELOG_MOD_COMMAND_LINE_PRINT:
            self.reprint(self.Printer(self.START_FROM_CMDLINE),_type=self.BELOG_PRINT_FORMATS["INFO"])
        elif self.mod == self.BELOG_MOD_FILE_WRITE:
            self.reprint(self.Printer(self.START_FROM_FILEWRITE),_type=self.BELOG_PRINT_FORMATS["INFO"])
            self.log_file = open(log_name+'.belog','w')
        else:
            raise InvalidMODError ("INVALID MOD, YOU CAN FIND MODS IN BELOG_MOD_....")
    def _istrue_s_color(self,s_color):
        if s_color in self._link_to_colors:
            return True
        else:
            return False
    def _istrue_b_color(self,b_color):
        if b_color in self._link_to_bcolors:
            return True
        else:
            return False
    def log(self,logText:str,print_func=print,_type='[INFO]'):
        if self.mod == self.BELOG_MOD_COMMAND_LINE_PRINT:
            print_func(_type,logText)
        elif self.mod == self.BELOG_MOD_FILE_WRITE:
            self.log_file.write(_type+logText+'\n')
        else:
            raise EtuExceptionError ()
    def give_log_file(self):
        return self.log_file
    def close_log_file(self):
        self.log_file.close()
        return True
    def remove_log(self):
        del self
        return True
    def Printer(self,code:dict):
        output = {}
        output['et'] = '\n'
        outText = ''
        for i in code:
            if i == 's_color':
                if not self._istrue_s_color(code['s_color']):
                    raise InvalidPrinterArgumentError("Argument [s_color] Is NOt Valid!")
                elif self._istrue_s_color(code['s_color']):
                    outText += code['s_color']
                else:
                    raise UnkownError()
            elif i == 'b_color':
                if not self._istrue_b_color(code['b_color']):
                    raise InvalidPrinterArgumentError("Argument [b_color] Is NOt Valid!")
                elif self._istrue_b_color(code['b_color']):
                    outText += code['b_color']
                else:
                    raise UnkownError()
            elif i == 's_text':
                if type(code['s_text']) != str:
                    raise InvalidPrinterArgumentError("Argument [s_text] Is NOt Valid!")
                elif type(code['s_text']) == str:
                    outText += code['s_text']
                else:
                    raise UnkownError()
            elif i == 'text':
                if type(code['text']) != str:
                    raise InvalidPrinterArgumentError("Argument [text] Is NOt Valid!")
                elif type(code['text']) == str:
                    outText += code['text']
                else:
                    raise UnkownError()
            elif i == 'e_text':
                if type(code['e_text']) != str:
                    raise InvalidPrinterArgumentError("Argument [e_text] Is NOt Valid!")
                elif type(code['e_text']) == str:
                    output['et'] = code['e_text']
                else:
                    raise UnkownError()
            elif i == 'e_color':
                if not self._istrue_s_color(code['e_color']):
                    raise InvalidPrinterArgumentError("Argument [e_color] Is NOt Valid!")
                elif self._istrue_s_color(code['e_color']):
                    outText += code['e_color']
                else:
                    raise UnkownError()
            elif i == 'eb_color':
                if not self._istrue_b_color(code['eb_color']):
                    raise InvalidPrinterArgumentError("Argument [eb_color] Is NOt Valid!")
                elif self._istrue_b_color(code['eb_color']):
                    outText += code['eb_color']
                else:
                    raise UnkownError()
            elif i == 'method':
                newOut = ''
                for c in outText:
                    newOut += code['method'](c)
                outText = newOut
            elif i == 'flush':
                output['flush'] = code['flush']
            elif i == 'flushed':
                output['flushed'] = code['flushed']
            elif i == 'unicode':
                outText = outText.encode(code['unicode'])
            else:
                pass
        output['text'] = outText
        return output
    def _first(self,_t='info'):
        if _t == 'info':
            INFO_FORMATING = f'{self._class_correct_value["INFO"]}[{Back.MAGENTA}INFO{Back.RESET}]{Fore.RESET} '
            return INFO_FORMATING
        elif _t == 'warning':
            WARNING_FORMATING = f'{self._class_correct_value["WARNING"]}[{Back.WHITE}WARNING{Back.RESET}]{Fore.RESET} '
            return WARNING_FORMATING
        elif _t == 'cirtical':
            CIRTICAL_FORMATING = f'{self._class_correct_value["CIRTICAL"]}[{Back.RED}CIRTICAL{Back.RESET}]{Fore.RESET} '
            return CIRTICAL_FORMATING
        else:
            raise Exception ()
        
    def _C_f(self,code:dict):
        f=0
        fed=0
        for i in code:
            if i == 'flush':
                f = 1
            elif i == 'flushed':
                fed = 1
            else:
                pass
                
        return f,fed
    
    def reprint(self,_dict:dict,_type=BELOG_PRINT_FORMATS['INFO']):
        if _type == belog.BELOG_PRINT_FORMATS['INFO']:
            first = self._first('info')
            if self._C_f(_dict)[0] and self._C_f(_dict)[1]:
                print(first,_dict['text'],flush=True,end='\r')
            elif self._C_f(_dict)[0] and not self._C_f(_dict)[1]:
                print(first,_dict['text'],flush=True,end=_dict['et'])
            elif not self._C_f(_dict)[0] and self._C_f(_dict)[1]:
                print(first,_dict['text'],end='\n')
            elif not self._C_f(_dict)[0] and not self._C_f(_dict)[1]:
                print(first,_dict['text'],end=_dict['et'])
        elif _type == belog.BELOG_PRINT_FORMATS['WARNING']:
            first = self._first('warning')
            if self._C_f(_dict)[0] and self._C_f(_dict)[1]:
                print(first,_dict['text'],flush=True,end='\r')
            elif self._C_f(_dict)[0] and not self._C_f(_dict)[1]:
                print(first,_dict['text'],flush=True,end=_dict['et'])
            elif not self._C_f(_dict)[0] and self._C_f(_dict)[1]:
                print(first,_dict['text'],end='\n')
            elif not self._C_f(_dict)[0] and not self._C_f(_dict)[1]:
                print(first,_dict['text'],end=_dict['et'])
        elif _type == belog.BELOG_PRINT_FORMATS['CIRTICAL']:
            first = self._first('cirtical')
            if self._C_f(_dict)[0] and self._C_f(_dict)[1]:
                print(first,_dict['text'],flush=True,end='\r')
            elif self._C_f(_dict)[0] and not self._C_f(_dict)[1]:
                print(first,_dict['text'],flush=True,end=_dict['et'])
            elif not self._C_f(_dict)[0] and self._C_f(_dict)[1]:
                print(first,_dict['text'],end='\n')
            elif not self._C_f(_dict)[0] and not self._C_f(_dict)[1]:
                print(first,_dict['text'],end=_dict['et'])
        else:
            raise Exception ("Invalid Argument!")

class learn_Class():
    def __init__(self):
        ...
    def example(self):
        return "obj4mk_class = Class(\"MyClass\",functions={\"__init__\" : {\"name\" : \"__init__\",\"args\" : (\"self\",),\"lines\" : [\"print(\'Hello Class!\')\"]}})"
    def how2use(self):
        return "h2u:\nClass_Arguments=(class_name->String,class_erase->DontChange,functions->Dict:{functionName : {name : NameOfFunction->str,args : argumentsName->tuple[str], lines : linesOfFunction->List[str] }})"
    def help(self):
        return 'use:\nlearn.example|learn.how2use'


@cclass
class Class():
    def __init__(self,class_name,class_erase=['object'],functions={"__init__" : {"name" : "__init__","args":("self",),"lines":["self.by = 'etu.Class'","print(self.name)"]}}):
        self.ClassName = class_name
        self.ClassErase = class_erase
        self.kwargs = functions
        self.ClassStatic = {"ClassCode" : str(stdn.random.randint(987654321,1234567890))}
        self._readyfuncs = [nothing]
        self._funcs = []
        self.__Readyed = False
        self._func_format = {"name" : "__example__","args" : (self,) , "lines" : ["print(1010101)"]}
        self.__log = []
    def create_func(self,name_of_func:str,args:tuple,lines:list):
        for i in range(len(lines)):
            lines[i] = '\t' + lines[i]
        func = function(name_of_func,list(args),variables={},lines=lines).__repr__()
        self._funcs.append(func)
    def __ReadDict(self,dictof:dict):
        try:
            name = dictof['name']
            args = tuple(dictof['args'])
            lines = dictof['lines']
        except Exception as err:
            return False
            self.__log.append(err)
            raise Exception (err)
        self.create_func(name,args,lines)
        return True
    def __ready(self):
        for i in self.kwargs:
            self.__ReadDict(self.kwargs[i])
        self.__Readyed = True
    def SET(self):
        print("Seting Class")
        def Test(String:str):
            try:
                exec(String)
                return True
            except:
                return False
        if not self.__Readyed:
            self.__ready()
        tbn = '\n\t'
        first = str(f"class {self.ClassName}(")
        for erase in self.ClassErase:
            first+=str(erase)+','
        first += "):" + tbn
        Test(first+"pass")
        for i in self._funcs:
            first += i + tbn
        self.com = first
        return True
    def exe(self):
        print("Start Making...")
        self.SET()
        exec(self.com,globals())
        exec(f"_Class__NoneSpaceGlob = {self.ClassName}",globals())
        return __NoneSpaceGlob
    def run(self):
        return self.exe()()
    def __repr__(self):
        try:
            return str(self.com)
        except:
            self.exe()
            try:
                return str(self.com)
            except Exception as err:
                raise Exception(err)



def sfunction(name:str,p_String:str):
    exec(p_String,globals())
    exec(f"__NoneSpaceGlob = {name}",globals())
    return __NoneSpaceGlob

def sclass(name:str,p_String:str):
    exec(p_String,globals())
    exec(f"__NoneSpaceGlob = {name}",globals())
    return __NoneSpaceGlob


class File:
    def __init__(self,fpath):
        self._fpath = stdn.pathlib.Path(fpath) if (stdn.pathlib.Path(fpath)).exists() and (stdn.pathlib.Path(fpath).is_file()) else None
        if not self._fpath:
            raise FileNotFoundError ("")
        self.set_infobypath(self._fpath)
    def set_infobypath(self,fpath:stdn.pathlib.Path):
        if type(fpath) == str:
            fpath = stdn.pathlib.Path(fpath)
        self._fpath = fpath if (fpath).exists() and (fpath).is_file() else None
        if not self._fpath:
            raise FileNotFoundError ("")
        self._fname = fpath.name
        self._fsuffix = fpath.suffix
    def send_info(self):
        return {"file-name":self._fname,"file-suffix":self._fsuffix,"file-path":str(self._fpath.absolute())}

class dotPy:
    def __init__(self,file):
        if type(file) != File:
            raise TypeError (f"Invalid Type Of Object. {File}")
        self._modules = []
        self._info = file.send_info()
    def run(self,switch=''):
        stdn.os.system(sys.executable+' '+self._info['file-path']+' '+switch)
        return 1
    def import_file(self)->type(sys):
        _path = pl.Path(self._info['file-path']).parent
        sys.path.append(str(_path))
        return stdn.importlib.import_module(self._info['file-name'].strip('.py'))

class dotJson:
    def __init__(self,file):
        if type(file) != File:
            raise TypeError (f"Invalid Type Of Object. {File}")
        
        self._info = file.send_info()
    def read(self):
        return stdn.json.load(open(self._info['file-path']))
    def readstr(self):
        return open(self._info['file-path']).read()
    def readpy(self):
        return eval(open(self._info['file-path']).read())

def Exec(string):
    try:
        exec(string,globals())
    except Exception as err:
        raise Exception (err)
    return True




@cclass
class cfs:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.flag = 0
    def sum(self):
        return self.x + self.y
    def __repr__(self):
        return f'x:{self.x} - y:{self.y}'
    def setX(self,x:int):
        self.x = x
        return self.x
    def setY(self,y:int):
        self.y = y
        return self.y
    def addX(self,x=1):
        self.x += x
        return self.x
    def addY(self,y=1):
        self.y += y
        return self.y
    def subX(self,x=1):
        self.x -= x
        return self.x
    def subY(self,y=1):
        self.y -= y
        return self.y
    def xorX(self,x:int):
        self.x ^= x
        return self.x
    def xorY(self,y:int):
        self.y ^= y
        return self.y
    def print(self):
        fp = self.__repr__()
        print(fp)
        return None
    def mulX(self,x:int):
        self.x *= x
        return self.x
    def mulY(self,y:int):
        self.y *= y
        return self.y
    def floordivX(self,x:int):
        self.x //= x
        return self.x
    def floordivY(self,y:int):
        self.y //= y
        return self.y
    def invX(self,set=False):
        if set == True:
            self.x = ~self.x
            return self.x
        else:
            return ~self.x
    def invY(self,set=False):
        if set == True:
            self.y = ~self.y
            return self.y
        else:
            return ~self.y
    def modX(self,x:int):
        self.x %= x
        return self.x
    def modY(self,y:int):
        self.y %= y
        return self.y
    def negX(self,set=False):
        if set == True:
            self.x = -self.x
            return self.x
        else:
            return -self.x
    def negY(self,set=False):
        if set == True:
            self.y = -self.y
            return self.y
        else:
            return -self.y
    def posX(self,set=False):
        if set == True:
            self.x = +self.x
            return self.x
        else:
            return +self.x
    def posY(self,set=False):
        if set == True:
            self.y = +self.y
            return self.y
        else:
            return +self.y
    def powX(self,x:int):
        self.x **= x
        return self.x
    def powY(self,y:int):
        self.y **= y
        return self.y
    def truedivX(self,x:int):
        self.x /= x
        return self.x
    def truedivY(self,y:int):
        self.y /= y
        return self.y
    def isX(self,x:int):
        return self.x is x
    def isnotX(self,x:int):
        return self.x is not x
    def isY(self,y:int):
        return self.y is y
    def isnotY(self,y:int):
        return self.y is not y
    def rshiftX(self,x:int):
        self.x >>= x
        return self.x
    def lshiftX(self,x:int):
        self.x <<= x
        return self.x
    def rrshiftX(self,x:int,x2:int):
        self.x >>= x >> x2
        return self.x
    def rlshiftX(self,x:int,x2:int):
        self.x <<= x >> x2
        return self.x
    def rshiftY(self,y:int):
        self.y >>= y
        return self.y
    def lshiftY(self,y:int):
        self.y <<= y
        return self.y
    def rrshiftY(self,y:int,y2:int):
        self.y >>= y >> y2
        return self.y
    def rlshiftY(self,y:int,y2:int):
        self.y <<= y >> y2
        return self.y
    #===================================================
    def addXX(self):
        self.x += self.x
        return self.x
    def addYY(self):
        self.y += self.y
        return self.y
    def subXX(self):
        self.x -= self.x
        return self.x
    def subYY(self):
        self.y -= self.y
        return self.y
    def xorXX(self):
        self.x ^= self.x
        return self.x
    def xorYY(self):
        self.y ^= self.y
        return self.y
    def mulXX(self):
        self.x *= self.x
        return self.x
    def mulYY(self):
        self.y *= self.y
        return self.y
    def floordivXX(self):
        self.x //= self.x
        return self.x
    def floordivYY(self):
        self.y //= self.y
        return self.y
    def modXX(self):
        self.x %= self.x
        return self.x
    def modYY(self):
        self.y %= self.y
        return self.y
    def powXX(self):
        self.x **= self.x
        return self.x
    def powYY(self):
        self.y **= self.y
        return self.y
    def truedivXX(self):
        self.x /= self.x
        return self.x
    def truedivYY(self):
        self.y /= self.y
        return self.y
    def XeqY(self):
        return self.x == self.y
    def XnqY(self):
        return self.x != self.y
    def rshiftXX(self):
        self.x >>= self.x
        return self.x
    def lshiftXX(self):
        self.x <<= self.x
        return self.x
    def rrshiftXX(self,x:int):
        self.x >>= self.x >> x
        return self.x
    def rlshiftX(self,x:int):
        self.x <<= self.x >> x
        return self.x
    def rshiftY(self):
        self.y >>= self.y
        return self.y
    def lshiftY(self):
        self.y <<= self.y
        return self.y
    def rrshiftY(self,y:int):
        self.y >>= self.y >> y
        return self.y
    def rlshiftY(self,y:int):
        self.y <<= self.y >> y
        return self.y
    #=====================================================
    def addXY(self):
        self.flag = self.x + self.y
        return self.flag
    def subXY(self):
        self.flag = self.x - self.y
        return self.flag
    def subYX(self):
        self.flag = self.y - self.x
        return self.flag
    def xorXY(self):
        self.flag = self.x ^ self.y
        return self.flag
    def xorYX(self):
        self.flag = self.y ^ self.x
        return self.flag
    def mulXY(self):
        self.flag = self.x * self.y
        return self.flag
    def mulYX(self):
        self.flag = self.y * self.x
        return self.flag
    def floordivXY(self):
        self.flag = self.x // self.y
        return self.flag
    def floordivYX(self):
        self.flag = self.y // self.x
        return self.flag
    def modXY(self):
        self.flag = self.x & self.y
        return self.flag
    def modYX(self):
        self.flag = self.y % self.x
        return self.flag
    def powXY(self):
        self.flag = self.x ** self.y
        return self.flag
    def powYX(self):
        self.flag = self.y ** self.x
        return self.flag
    def truedivXY(self):
        self.flag = self.x / self.y
        return self.x
    def truedivYX(self):
        self.flag = self.y % self.x
        return self.flag
    def rshiftXY(self):
        self.flag = self.x >> self.y
        return self.flag
    def lshiftXY(self):
        self.flag = self.x << self.y
        return self.flag
    def rrshiftXY(self,x:int):
        self.flag = self.x >> self.y >> x
        return self.flag
    def rlshiftXY(self,x:int):
        self.flag = self.x << self.y >> x
        return self.flag
    def rshiftYX(self):
        self.flag = self.y >> self.x
        return self.flag
    def lshiftYX(self):
        self.flag = self.y << self.x
        return self.flag
    def rrshiftYX(self,y:int):
        self.flag = self.y >> self.x >> y
        return self.flag
    def rlshiftYX(self,y:int):
        self.flag = self.y << self.x >> y
        return self.flag
    
    



@cclass
class new():
    def __init__(self,ObjTN):
        self.__cject = ObjTN
        self.__tp = type(ObjTN)
        if type(type(ObjTN)) == type:
            super(new,self).__init__()
            self.val = self.__tp(ObjTN)
        else:
            raise TypeError ('Invalid Type!\nExampleUse : new(int(4))')
    def __repr__(self):
        return f"{new} [-] <Value {str(type(self.__cject))} {self.val}>"
    def dot(self):
        return self.__cject
    def type_dot(self):
        return self.__tp
    def __call__(self):
        return self.__cject

_xy = cfs()


@cfunc 
def printc(text:str,ctext:str,timesleep=0.2):
    print(text,end='\r')
    stdn.time.sleep(timesleep)
    print(ctext,end='')


@cclass
class AnimationGraph(): 
    def __init__(self,fode=[0,100]):
        import pyfiglet as __pyf
        self.Fonts = __pyf.FigletFont().getFonts()[fode[0]:fode[1]]
        self.Figlet = __pyf.Figlet
        self._vFont = self.Fonts[stdn.random.randint(fode[0],fode[1]-1)]
    def setFont(self,fontn:int):
        self._vFont = self.Fonts[fontn]
    def ReadFonts(self):
        return self.Fonts
    def EasyGraph(self,text):
        fRend = self.Figlet(self._vFont,text)
        Rended = fRend.renderText(text)
        return Rended
    def event(self):
        import keyboard as kb
        while True:
            break #-----------------------> HERE
    def RenderGraphText(self,bText:str):
        pass

@cclass
class AnimationLoader():
    def __init__(self,backText="loading",nextText=None,loaderlength:int=1,loaderstyle={"color":Fore.GREEN,"BackGround":Back.WHITE},end='\n'):
        self.bt = backText
        self.nt = nextText
        self.ll = loaderlength
        self.ls = loaderstyle
    def printf(self,text:str):
        print(text,end='\r',flush=True)
    def anim(self,sleep=0.8):
        li = ''
        self.load = ""
        if self.nt != None:
            self.load += self.ls['color']+self.bt+Fore.RESET+' '
            li+=self.ls['BackGround']
            self.printf(self.load)
            for i in range(self.ll):
                li+=' '
                self.load+=li+Back.RESET
                stdn.time.sleep(sleep)
                self.printf(self.load)
            li+=Back.RESET
            li+=self.ls['color']
            li+=self.nt
            li+=Fore.RESET
            self.load += li 
            self.printf(self.load)
        else:
            self.load += self.ls['color']+self.bt+Fore.RESET+' '
            li+=self.ls['BackGround']
            self.printf(self.load)
            for i in range(self.ll):
                li+=' '
                self.load+=li+Back.RESET
                stdn.time.sleep(sleep)
                self.printf(self.load)
            li+=Back.RESET
            self.load += li
            self.printf(self.load)

@cfunc
def easy_loading(text='loading',armor='[',armorb=']',sleep=0.1,loader='-',range_=10):
    text = text +' '+ armor
    for i in range(range_):
        print(text+armorb,end='\r',flush=True)
        text += loader
        stdn.time.sleep(sleep)
    print(text+armorb,end='\n')

@cclass
class LoadingAnimation():
    defualt_color = Fore.WHITE
    def __init__(self):
        self._realanimation = {"act" : [], "anime" : [],"end" : []}
        self._realhelp = {"pr" : "print","fl":"flush"}
    def addAnime(self,animeText:str,act='fl',end='',c:Fore=Fore.GREEN,ce:Fore=Fore.RESET):
        self._realanimation['anime'].append(c+animeText+ce)
        self._realanimation['act'].append(act)
        self._realanimation['end'].append(end)
        return True
    def addList(self,l:dict):
        end=l['end']
        anime=l['anime']
        act=l['act']
        def APPEND(ls,tp):
            for i in ls:
                self._realanimation[tp].append(i)
        APPEND(end,'end')
        APPEND(anime,'anime')
        APPEND(act,'act')
        return True
    def addListSecure(self,l:dict):
        end=l['end']
        act=l['act']
        anime=l['anime']
        try:
            for i in range(len(anime)):
                self._realanimation['anime'].append(anime[i])
                self._realanimation['act'].append(act[i])
                self._realanimation['end'].append(end[i])
        except Exception as err:
            raise Exception (err)
        return True
    def printf(self,text:str,flush=True,end=''):
        print(text,flush=flush,end=end)
    def make(self):
        self._zip = self._realanimation['anime']
        self._act = self._realanimation['act']
        self._end = self._realanimation['end']
        return True
    def get(self)->dict:
        return {"animationsStep":self._zip,"actions":self._act,"end":self._end}
    def printAnimation(self):
        read = self._zip
        readact = self._act
        End = self._end
        for i in range(len(read)):
            if readact[i].upper() == "FL":
                print(read[i],flush=True,end=End[i])
            elif readact[i].upper() == "FLF":
                self.printf(read[i],flush=True,end=End[i])
            elif readact[i].upper() == "PR":
                print(read[i],end=End[i])
            elif readact[i].upper() == "FPR":
                self.printf(read[i],end=End[i])
            else:
                raise TypeError (f"Can't Use ActionType({readact[i]})!")

@cclass
class AnimationText():
    def __init__(self):
        self._antxt = None
        self._antxt_e = None
        self.list = []
    def set_animation(self,ls:list):
        self.list = ls
    def make_animation(self,func=lambda x:x):
        o = list()
        for i in self.list:
            o.append(func(i))
        self.outAnimation = o
        return o
    def wAnimationPrint(self):
        for i in self.outAnimation:
            yield i
    def set_text(self,text:str):
        self._antxt = text
        return True
    def set_end_text(self,text:str):    
        self._antxt_e = text
        return True
    def AnimationPrint(self,type="loader",timesleep=0.25):
        if type == 'loader':
            alist = self.outAnimation
            print(alist[0],end='\r')
            for i in alist[1:]:
                print(i,end='\r',flush=True)
                stdn.time.sleep(timesleep)
        elif type == 'times':
            alist = self.outAnimation
            for i in alist:
                print(i,end='')
                stdn.time.sleep(timesleep)
        elif type == 'master':
            def make_text(txt:str,ptr:str):
                return txt+ptr
            if self._antxt and self._antxt_e:
                alist = self.outAnimation
                for i in alist[:-1]:
                    print(make_text(self._antxt,i),end='\r',flush=True)
                    stdn.time.sleep(timesleep)
                print(make_text(self._antxt,alist[-1])+self._antxt_e+'\t'*5,end='\n')
            else:
                self.AnimationPrint(timesleep=timesleep)
class Vbin():
    def __init__(self,objecute:list):
        self.obj = objecute
    def __repr__(self):
        cb = str(self.obj).strip('[').rstrip(']').split(',')
        zx = ''
        for i in cb:
            zx += str(i) + '  '
        return zx
    def __format__(self,obj):
        return self.__repr__()
    def __delattr__(self,name,obj):
        delattr(obj,name)
    def __getitem__(self,item):
        if type(item) is not int:
            raise TypeError ("Invalid Type.")
        return self.obj[item]


function('SunNum',["text:str","gq='x'"],{"OMGFLAG": True,"output":[]},["for i in range(len(str(text))):output.append(str(text).replace(str(text)[i],gq))",'return output']).exe()

function('SensorInt',['Num:int','SL:int'],{'L':'len(str(Num))','SR':'str(Num)','SRD':'SR[SL:]','SRD2':'SR[:SL]','flag':0},['for i in range(len(SRD)):flag+=1','for i in range(flag):SRD2+=\'*\'','return SRD2']).exe()

function('rtu_anloader',['text','etext','anim_len'],{'a': "AnimationText()"},['a.set_animation(["/","-","\\\\"]*anim_len+["~"])','a.set_text(text)','a.set_end_text(etext)','a.make_animation()','return a']).exe()
@cfunc
def AnimationPrint(alist:list,timesleep=0.25):
    print(alist[0],end='\r')
    for i in alist[1:]:
        print(i,end='\r',flush=True)
        stdn.time.sleep(timesleep)


def MiniTime(s,f):
    def stdf():
        print('\a',end='')
    def sett(s):
        time.sleep(s)
        f()
    stdn.threading.Thread(target=sett,args=(s,))

def Test_BForce(a,b,c,d,e,f):
    TEST_COMPUTING_SPEED = 2.
    while True:
        g = stdn.random.randint(e,f+e)
        if (a+b+c+g)==(d+e+f):
            return g


