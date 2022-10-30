import threading as _threading
from sys import getsizeof as sizeof
_defined_object = {}

class _function():
    options = ['name:str','args=[]','variables={}','lines=[]','function(name="Example",args=["Name"],variables={"GetName":"Name"},lines=["print(GetName)"])']

    def __init__(self,name:str,args=[],variables={},lines=['pass']):
        self.name = name
        self.args = args
        self.vars = variables
        self.lines = lines
    def run(self,args=()):
        runned = _threading.Thread(target=self.exe(),args=args)
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
def _exec(code):
    exec(code,globals())
class _Class():
    def __init__(self,class_name,class_erase=['object'],functions={"__init__" : {"name" : "__init__","args":("self",),"lines":["self.by = 'etu.Class'","print(self)"]}}):
        import random
        self.ClassName = class_name
        self.ClassErase = class_erase
        self.kwargs = functions
        self.ClassStatic = {"ClassCode" : str(random.randint(987654321,1234567890))}
        self._readyfuncs = []
        self._funcs = []
        self.__Readyed = False
        self._func_format = {"name" : "__example__","args" : (self,) , "lines" : ["print(1010101)"]}
        self.__log = []
    def create_func(self,name_of_func:str,args:tuple,lines:list):
        for i in range(len(lines)):
            lines[i] = '\t' + lines[i]
        func = _function(name_of_func,list(args),variables={},lines=lines).__repr__()
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
        print("Setting Class")
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


class cbs():
    def __init__(self,name:str,**objects):
        self._name=name
        self._objs = objects
        self._create()
    def _create(self):
        out = {}
        for i in self._objs.keys():
            out[i] = {"name" : i ,"args":('self',),"lines":[f"return {self._objs[i]}"]}
        self._structTranslated2Class = _Class(self._name,functions=out)
    def __call__(self,object):
            return self._structTranslated2Class.exe()
classbystruct = cbs;

class rstruct():
    def __init__(self,objects):
        self.__setmems(objects)
    def __setmems(self,mems):
        for i in mems.keys():
            setattr(self,i,mems[i])

class struct():
    def __init__(self,**objects):
        self.__objects = objects
    def __call__(self):
        for i in self.__objects.keys():
            self.__objects[i] = None
        new = rstruct(self.__objects)
        return new

class define:
    def __init__(self,object,value):
        self.tdef(object,value)
    def tdef(self,object,value):
        _exec(f"{object} = {value}")
        _defined_object[str(object)] = value

class ifdef:
    def __init__(self,object):
        if str(object) in _defined_object.keys():
            self.defined = True
        else:
            self.defined = False
    def define(self,object,value):
        if self.defined:
            define(object,value)



class ifndef:
    def __init__(self,object):
        if str(object) in _defined_object.keys():
            self.defined = False
        else:
            self.defined = True
    def define(self,object,value):
        if not self.defined:
            define(object,value)


class defifndef:
    def __init__(self,object,value,objectfdef):
        ifndef(objectfdef).define(object,value)

class defifdef:
    def __init__(self,object,value,objectfdef):
        ifdef(objectfdef).define(object,value)

def defined_objects():
    return _defined_object
