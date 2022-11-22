""" OMG LIB VERSION 0.0.1
"""
""" Simple Lib Compiler FExample (xor,plus,sub,mul,flrd)
xor(3,3,3,3,3,3,3,3,3,3);SimpleRuner();
"""
""" About Compiler
SCODE -> Compiler(ToPyExecRunFormat) -> PYEXEC -> Read(PYEXEC)[ret][()]
"""
#-------------------------- OMGLAN SUPER FUNCTION's
exec("""
def ret(*args):
    return args
""")

exec("""
p = print;
pout = print;
bn = '\\n';
bb = '\\\\';
br = '\\r';
""")

def ToStringList(ls):
    outS = ''
    for i in ls:
        outS += i
    return outS
    

class function():
    def __init__(self,name:str,args=[],variables={},lines=["pass"]):
        self.name = name
        self.args = args
        self.vars = variables
        self.lines = lines
    def run(self,args={}):
        globals()
        __cx = self.exe()
        __CX = __cx
        sargs = str(args)
        sargs = sargs.strip("{").rstrip("}").replace(":","=").replace("\"","")
        exec("exec(f\"{out = __cx(\{sargs\})}\")",globals())
        return out
    def ___make(self):
        out = "def "
        print("Start Making...")
        defName = "def {}(): pass"
        defArgs = "def {}({}): pass"
        defVar = "{} = {}"
        defLine = "def {}({}):"
        nx = "\n\t"
        defArgs_t = ""
        try:
            for i in self.name:
                if " " in self.name:
                    self.name.strip(" ")
            try:
                exec(f"{defName.format(self.name)}")
            except Exception as err:
                raise NoneSpaceSyntaxError (err)
            for i in self.args:
                defArgs_t += f"{i},"
            try:
                exec(defArgs.format(self.name,defArgs_t))
            except Exception as err:
                raise NoneSpaceSyntaxError (err)
            formating = defLine.format(self.name,defArgs_t) + nx
            for i in self.vars:
                if type(i) is not str:
                    raise IReturnValueError (f"Value Invalid Type Of VariableName {i} In {self.vars} Can\"t Set Variable In Program")
                if " " in i:
                    raise NoneSpaceSyntaxError (f"Invalid Syntax Of VariableName {i}.")

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
                defLine += "pass"
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
            print("Warning: CVS-ERROR")
        main = "def {}({}):"

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

def DEFINE(var,val):
    exec(f"{var}={val}",globals())
    return True
#-------------------------

exec("""
def insertlib(modulepath:str):
    with open(modulepath,'r') as mdl:
        source = mdl.read()
        mdl.close()
    exec(source,globals())
""")

exec("""
def importpy(module:str,mod:'exe' or 'modulename' = 'modulename'):
    if mod == 'exe':
        exec(module,globals())
    else:
        from importlib import import_module
        return import_module(module)
""")

exec("""
def lenofile(filepath:str):
    with open(filepath,'r') as f:
        content = f.read()
        f.close()
    return len(content)
""")

#-------------------------------- Operators

def sub(*args):
    old = args[0]
    for i in list(args)[1:]:
        out = old - i
        old = out
    return out

def xor(*args):
    old = args[0]
    for i in list(args)[1:]:
        out = old ^ i
        old = out
    return out

def plus(*args):
    old = args[0]
    for i in list(args)[1:]:
        out = old + i
        old = out
    return out
    
def sub(*args):
    old = args[0]
    for i in list(args)[1:]:
        out = old - i
        old = out
    return out

def mul(*args):
    old = args[0]
    for i in list(args)[1:]:
        out = old * i
        old = out
    return out

def flrd(*args):
    old = args[0]
    for i in list(args)[1:]:
        out = old / i
        old = out
    return out

#--------------------------
class CSourceInvalidMod(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class CSourceInvalidValue(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class ReturnNotFoundError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        

class compilesc():
    def __init__(self,csourse):
        self.csc = csourse
        self.inlined = False
    def import_(self,modulec,mdl=None):
        if mdl != None:
            exec(f"global {mdl}",globals())
        exec (f"import {modulec}",globals())
    def run_term(self,term):
        return self.compile_intershell(term)
    def intershell(self,outer=False):
        import keyboard as kb
        flag = True
        while flag:
            term = input("OMGSHELL-> ")
            if outer:
                term = 'p('+term+');'
            print("Out: ",self.run_term(term))
            if term == "exit":
                flag = False
        return True
    def shell_error(self,msg):
        from colorama import Fore,init,deinit
        init()
        print(Fore.RED + str(msg) + Fore.RESET)
        deinit()
    def compile_intershell(self,source):
        self.csc = source
        mod = 'fsource'
        self._replaceobj()
        self._linecap()
        try:
            self.pyexe(mod)
        except Exception as err:
            self.shell_error(err)
            return False
        return True
    def compile(self,mod='fsource',v:'ret' or 'non'='non'):
        if self.inlined == True:
            if v == 'non':
                self.pyexe(mod)
            elif v == 'ret':
                self.pyexe(mod)
                self._rets = f""" # Source For Return Back Compiler Return's ;
    compilesc._return = function("__seed",lines=[\'return {self._rmbn(self._linedic(self.csc)[self._findret()])}\']).exe();"""
                self._compilesource(self._rets)
                return compilesc._return()
            else:
                raise CSourceInvalidValue ('Value Of v IsNotvalid!')
        else:
            if v == 'non':
                self._replaceobj()
                self._linecap()
                self.pyexe(mod)
                self.inlined = True
            elif v == 'ret':
                self._replaceobj()
                self._linecap()
                self.pyexe(mod)
                self.inlined = True
                self._rets = f""" # Source For Return Back Compiler Return's ;
    compilesc._return = function("__seed",lines=[\'return {self._rmbn(self._linedic(self.csc)[self._findret()])}\']).exe();"""
                self._compilesource(self._rets)
                return compilesc._return()
            else:
                raise CSourceInvalidValue ('Value Of v IsNotvalid!')
    def _rmbn(self,sc):
        return sc.replace('\n','')
    def pyexe(self,mod:'fsource' or 'lsource'):
        if mod == 'fsource':
            self._compilesource(self.csc)
        elif mod == 'lsource':
            for i in self.csl:
                self._compilesource(i)
        else:
            raise CSourceInvalidMod("Mod Setted IsNotValid!")
    def _findret(self):
        q = self._linedic(self.csc)
        for i in range(len(q)):
            if 'ret(' in q[i]:
                return i
        raise ReturnNotFoundError ("Compiler Can't Find Return Function!")
    def view_source(self):
        if self.inlined == True:
            return self.csc
        else:
            self._replaceobj()
            self._linecap()
            self.inlined = True
            return self.csc
    def _compilesource(self,source):
        exec(source,globals())
    def _linecap(self):
        self.csl = self._linedic(self.csc)
    def _linedic(self,sc):
        return sc.split(';')
    def compile_with_pyinstaller(self,outName,by_omegapy=True):
        from os import system
        if by_omegapy:
            self.make_py(outName)
            system(f'pyexe.exe {by_omegapy}')
        else:
            self.make_py(outName)
            system(f'pyinstaller {outName} --console --onefile --noconfirm --clean')
    def make_py(self,file_name:str):
        if self.inlined:
            with open(file_name+'.py','w') as f:
                f.write(self.csc)
                f.close()
            return True
        else:
            self.view_source()
            with open(file_name+'.py','w') as f:
                f.write(self.csc)
                f.close()
            return True
    def _replaceobj(self):
        self.csc = self._replaceCharDot(self.csc)
        self.csc = self._replaceCharLocalRepQuery(self.csc)
        self.csc = self._replaceCharbs(self.csc)
        self.csc = self._replaceCharBs(self.csc)
        self.csc = self._replaceCharPrint(self.csc)
        self.csc = self._replaceCharLocalFunction(self.csc)
        self.csc = self._replaceCharLocalClass(self.csc)
        self.csc = self._replaceFunc(self.csc)
        self.csc = self._replaceCharAddSine(self.csc)
        self.csc = self._replaceCharNotEq(self.csc)
        self.csc = self._replaceCharXor(self.csc)
        self.csc = self._replaceCharComment(self.csc)
        self.csc = self._replaceCharOpenFlow(self.csc)
        self.csc = self._replaceCharOpenFlow2(self.csc)
        self.csc = self._replaceCharBackSlashN(self.csc)
        self.csc = self._replaceCharQAdd(self.csc)
        
    def _replaceCharQAdd(self,sc):
        return sc.replace('$Query081','@')
    def _replaceCharOpenFlow(self,sc):
        return sc.replace('~{','(')
    def _replaceCharOpenFlow2(self,sc):
        return sc.replace('}~',')')
    def _replaceCharComment(self,sc):
        return sc.replace('//','#')
    def _replaceCharXor(self,sc):
        return sc.replace('&^','^')
    def _replaceCharDot(self,sc):
        return sc.replace('->','.')
    def _replaceFunc(self,sc):
        return sc.replace('func ','def ')
    def _replaceCharAddSine(self,sc):
        return sc.replace('@','')
    def _replaceCharNotEq(self,sc):
        return sc.replace('<>','!=')
    def _replaceCharLocalRepQuery(self,sc):
        return sc.replace('$Query501','')
    def _replaceCharBackSlashN(self,sc):
        return sc.replace('$Query100','\\n')
    def _replaceCharPrint(self,sc):
        return sc.replace('$Query100','print')
    def _replaceCharLocalFunction(self,sc):
        return sc.replace('$Query150','function')
    def _replaceCharLocalClass(self,sc):
        return sc.replace('$Query190','Class')
    def _replaceCharbs(self,sc):
        return sc.replace('$Query310','\\')
    def _replaceCharBs(self,sc):
        return sc.replace("\\",'\\\\')


def open_source(source_path:str):
    with open(source_path,'r') as source:
        source_inline = source.read()
        source.close()
        
    return compilesc(source_inline)
opensource = open_source




def import_omg(omg_path:str):
    with open(omg_path,'r') as source:
        sc = source.readlines()
        source.close()
    ot = []
    ot2 = []
    for i in sc:
        ot2.append(i)
    
    source_fc = ToStringList(ot2)
    a = compilesc(source_fc)
    ss_f = a.view_source().split('\n')
    for i in ss_f:
        ot.append('\t' + i)
    
    
    source = ToStringList(ot)
    exec(f"""
class omg():
    {source}
""",globals())
    return omg


def Exec(source,globals_=None,locals_=None):
    exec(source,globals_,locals_)

if __name__ == '__main__':
    import sys
    try:
        if sys.argv[1]:
            try:
                if sys.argv[2]:
                    open_source(sys.argv[1]).compile(v=sys.argv[2])
            except:
                open_source(sys.argv[1]).compile()
        else:
            pass
    except Exception as err:
        print(err)
