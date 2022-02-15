############  Public Modules

try:
    import numpy as np
    import pathlib as pl
    from colorama import init,Fore,Back,Style
except Exception as err:
    raise ImportError (err)

###############################################################################################
###############################################################################################


############  OMEGAPy Modules

try:
    from . import __need__ as stdn
except:
    try:
        from . import __need__
        stdn = __need__
    except Exception as err:
        raise ImportError (err)
        
###############################################################################################
###############################################################################################
init()

def nothing():pass


def int_(*args):
    return None


class _Learn():
    def __init__(self):
        self.__ex = self.example
        self.__h2u = self.how2use
        self.__hlp = self.help
    def example(self):
        return "LEARN.callobj(2)\nLEARN.endcall(2)\nLEARN.TASKDONE(LEARN.forever)"
    def how2use(self):
        return "this is an example for you\nprintf(\"Hello World\");"
    def help(self):
        return "LEARN WITH OOP!"

class Condition():
    def __init__(self,conditionStr:str):
        self.cs = conditionStr
    def _check(self):
        return self.cs

class c_for():
    def std_print(i):
        print(i)
    def __init__(self,i:int,condition:Condition,job:str,work:type(nothing)):
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
                int_a*=job[i+1]
            elif job[i]=='/':
                int_a/=job[i+1]
            elif job[i]=='**':
                int_a**=job[i+1]
            elif job[i]=='//':
                int_a//=job[i+1]
            elif job[i]=='%':
                int_a%=job[i+1]
            else:
                pass
        return int_a
    
class CoreException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class NoneSpaceSyntaxError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

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

class function():
    options = ['name:str','args=[]','variables={}','lines=[]','function(name="Example",args=["Name"],variables={"GetName":"Name"},lines=["print(GetName)"])']
        
    def __init__(self,name:str,args=[],variables={},lines=['pass']):
        self.name = name
        self.args = args
        self.vars = variables
        self.lines = lines
    def run(self,args={}):
        globals()
        __cx = self.exe()
        __CX = __cx
        sargs = str(args)
        sargs = sargs.strip('{').rstrip('}').replace(':','=').replace('\'','')
        exec("exec(f\"{out = __cx(\{sargs\})}\")",globals())
        return out
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

class UnkownError(Exception):
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
    def log(self,logText:str,print_function=print,_type='[INFO]'):
        if self.mod == self.BELOG_MOD_COMMAND_LINE_PRINT:
            print_function(_type,logText)
        elif self.mod == self.BELOG_MOD_FILE_WRITE:
            self.log_file.write(_type+logText+'\n')
        else:
            raise Exception ()
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

class learn_Class(_Learn):
    def __init__(self):
        super().__init__()
    def example(self):
        return "obj4mk_class = Class(\"MyClass\",functions={\"__init__\" : {\"name\" : \"__init__\",\"args\" : (\"self\",),\"lines\" : [\"print(\'Hello Class!\')\"]}})"
    def how2use(self):
        return "h2u:\nClass_Arguments=(class_name->String,class_erase->DontChange,functions->Dict:{functionName : {name : NameOfFunction->str,args : argumentsName->tuple[str], lines : linesOfFunction->List[str] }})"
    def help(self):
        return 'use:\nlearn.example|learn.how2use'

class Class():
    def __init__(self,class_name,class_erase=['object'],functions={"__init__" : {"name" : "__init__","args":("self",),"lines":["self.name = 'mamad'","print(self.name)"]}}):
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
        first = str(f"class {self.ClassName}(object):" + tbn)
        
        
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




def Exec(string):
    try:
        exec(string,globals())
    except Exception as err:
        raise Exception (err)
    return True





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
    
    

def data_mage(imgpath:pl.Path):
    from cv2 import imread
    img = imread(imgpath)
    imgA = np.array(img)
    return imgA


    
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


        
def printc(text:str,ctext:str,timesleep=0.2):
    print(text,end='\r')
    stdn.time.sleep(timesleep)
    print(ctext,end='')



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

def easy_loading(text='loading',armor='[',armorb=']',sleep=0.1,loader='-',range_=10):
    text = text +' '+ armor
    for i in range(range_):
        print(text+armorb,end='\r',flush=True)
        text += loader
        stdn.time.sleep(sleep)
    print(text+armorb,end='\n')


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
class AnimationText():
    def __init__(self):
        self.list = []
    def set_animation(self,ls:list):
        self.list = ls
    def make_animation(self,func):
        o = list()
        for i in self.list:
            o.append(func(i))
        self.outAnimation = o
        return o
    def wAnimationPrint(self):
        for i in self.outAnimation:
            yield i
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

def AnimationPrint(alist:list,timesleep=0.25):
    print(alist[0],end='\r')
    for i in alist[1:]:
        print(i,end='\r',flush=True)
        stdn.time.sleep(timesleep)



