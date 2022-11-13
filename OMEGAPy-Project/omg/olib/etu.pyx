# cython : embedsignature=True
# cython : language_level=3

# Modules
cimport cython



    

cpdef long int gtime(appn:str):
    from os import system
    from time import time
    def log(LOG:str):
        print(LOG)
    cdef long int gt = time()
    system(appn)
    cdef long int get = time()
    log("Start Time %s" % str(gt))
    log("End Time %s" % str(get))
    log("\nTotal : %s" % str(get-gt))
    return get-gt


# class function():
#     options = ['name:str','args=[]','variables={}','lines=[]','function(name="Example",args=["Name"],variables={"GetName":"Name"},lines=["print(GetName)"])']
        
#     def __init__(self,name:str,args=[],variables={},lines=['pass']):
#         self.name = name
#         self.args = args
#         self.vars = variables
#         self.lines = lines
#     def run(self,args=()):
#         runned = stdn.threading.Thread(target=self.exe(),args=args)
#         runned.start()
#     def ___make(self):
#         out = 'def '
#         print('Start Making...')
#         defName = 'def {}(): pass'
#         defArgs = 'def {}({}): pass'
#         defVar = '{} = {}'
#         defLine = 'def {}({}):'
#         nx = '\n\t'
#         defArgs_t = ''
#         try:
#             for i in self.name:
#                 if ' ' in self.name:
#                     self.name.strip(' ')
#             try:
#                 exec(f'{defName.format(self.name)}')
#             except Exception as err:
#                 raise NoneSpaceSyntaxError (err)
#             for i in self.args:
#                 defArgs_t += f'{i},'
#             try:
#                 exec(defArgs.format(self.name,defArgs_t))
#             except Exception as err:
#                 raise NoneSpaceSyntaxError (err)
#             formating = defLine.format(self.name,defArgs_t) + nx
#             for i in self.vars:
#                 if type(i) is not str:
#                     raise IReturnValueError (f'Value Invalid Type Of VariableName {i} In {self.vars}\nCan\'t Set Variable In Program')
#                 if ' ' in i:
#                     raise NoneSpaceSyntaxError (f'Invalid Syntax Of VariableName {i}.')
                
#                 formating += defVar.format(i,self.vars[i]) + nx
#                 try:
#                     exec(formating)
#                 except Exception as err:
#                     raise NoneSpaceSyntaxError (err)
#             defLine = defLine.format(self.name,defArgs_t)
#             for i in self.vars:
#                 defLine += nx + defVar.format(i,self.vars[i])
#             defLine += nx
#             copy = defLine
#             if len(self.vars) == 0:
#                 defLine += 'pass'
#             try:
#                 exec(defLine)
#             except Exception as err:
#                 raise NoneSpaceSyntaxError (err)
#             defLine = copy
#             for i in self.lines:
#                 defLine += i + nx
#             try:
#                 exec(defLine)
#             except Exception as err:
#                 raise NoneSpaceSyntaxError (err)
                
#         except Exception as err:
#             print('Warning: CVS-ERROR')
#         main = 'def {}({}):'
        
#         for i in self.vars:
#             main += nx + defVar.format(i,self.vars[i])
#         main += nx
        
#         for i in self.lines:
#             main += i + nx
#         main = main.format(self.name,defArgs_t)
            
#         return main
#     @staticmethod
#     def execute(code):
#         exec(code)
#     def exe(self):
#         exec(self.___make(),globals())
#         exec(f"_function__NoneSpaceGlob = {self.name}",globals())
#         return __NoneSpaceGlob
#     def __repr__(self):
#         return self.___make()

    
        









# class Class():
#     def __init__(self,class_name,class_erase=['object'],functions={"__init__" : {"name" : "__init__","args":("self",),"lines":["self.by = 'etu.Class'","print(self.name)"]}}):
#         self.ClassName = class_name
#         self.ClassErase = class_erase
#         self.kwargs = functions
#         self.ClassStatic = {"ClassCode" : str(stdn.random.randint(987654321,1234567890))}
#         self._readyfuncs = [nothing]
#         self._funcs = []
#         self.__Readyed = False
#         self._func_format = {"name" : "__example__","args" : (self,) , "lines" : ["print(1010101)"]}
#         self.__log = []
#     def create_func(self,name_of_func:str,args:tuple,lines:list):
#         for i in range(len(lines)):
#             lines[i] = '\t' + lines[i]
#         func = function(name_of_func,list(args),variables={},lines=lines).__repr__()
#         self._funcs.append(func)
#     def __ReadDict(self,dictof:dict):
#         try:
#             name = dictof['name']
#             args = tuple(dictof['args'])
#             lines = dictof['lines']
#         except Exception as err:
#             return False
#             self.__log.append(err)
#             raise Exception (err)
#         self.create_func(name,args,lines)
#         return True
#     def __ready(self):
#         for i in self.kwargs:
#             self.__ReadDict(self.kwargs[i])
#         self.__Readyed = True
#     def SET(self):
#         print("Seting Class")
#         def Test(String:str):
#             try:
#                 exec(String)
#                 return True
#             except:
#                 return False
#         if not self.__Readyed:
#             self.__ready()
#         tbn = '\n\t'
#         first = str(f"class {self.ClassName}(")
#         for erase in self.ClassErase:
#             first+=str(erase)+','
#         first += "):" + tbn
#         Test(first+"pass")
#         for i in self._funcs:
#             first += i + tbn
#         self.com = first
#         return True
#     def exe(self):
#         print("Start Making...")
#         self.SET()
#         exec(self.com,globals())
#         exec(f"_Class__NoneSpaceGlob = {self.ClassName}",globals())
#         return __NoneSpaceGlob
#     def run(self):
#         return self.exe()()
#     def __repr__(self):
#         try:
#             return str(self.com)
#         except:
#             self.exe()
#             try:
#                 return str(self.com)
#             except Exception as err:
#                 raise Exception(err)



cpdef sfunction(name:str,p_String:str):
    exec(p_String,globals())
    exec(f"__NoneSpaceGlob = {name}",globals())
    return __NoneSpaceGlob

cpdef sclass(name:str,p_String:str):
    exec(p_String,globals())
    exec(f"__NoneSpaceGlob = {name}",globals())
    return __NoneSpaceGlob




def Exec(string):
    try:
        exec(string,globals())
    except Exception as err:
        raise Exception (err)
    return True




cpdef class cfs:
    cpdef void __init__(self,double x=0,double y=0):
        self.x = x
        self.y = y
        self.flag = 0
    cpdef double sum(self):
        return self.x + self.y
    cpdef __repr__(self):
        return f'x:{self.x} - y:{self.y}'
    cpdef double setX(self,x):
        self.x = x
        return self.x
    cpdef double setY(self,y):
        self.y = y
        return self.y
    cpdef double addX(self,x=1):
        self.x += x
        return self.x
    cpdef double addY(self,y=1):
        self.y += y
        return self.y
    cpdef double subX(self,x=1):
        self.x -= x
        return self.x
    cpdef double subY(self,y=1):
        self.y -= y
        return self.y
    cpdef double xorX(self,x:int):
        self.x ^= x
        return self.x
    cpdef double xorY(self,y:int):
        self.y ^= y
        return self.y
    cpdef print(self):
        fp = self.__repr__()
        print(fp)
        return None
    cpdef double mulX(self,x:int):
        self.x *= x
        return self.x
    cpdef double mulY(self,y:int):
        self.y *= y
        return self.y
    cpdef double floordivX(self,x:int):
        self.x //= x
        return self.x
    cpdef double floordivY(self,y:int):
        self.y //= y
        return self.y
    cpdef invX(self,set=False):
        if set == True:
            self.x = ~self.x
            return self.x
        else:
            return ~self.x
    cpdef invY(self,set=False):
        if set == True:
            self.y = ~self.y
            return self.y
        else:
            return ~self.y
    cpdef double modX(self,x:int):
        self.x %= x
        return self.x
    cpdef double modY(self,y:int):
        self.y %= y
        return self.y
    cpdef negX(self,set=False):
        if set == True:
            self.x = -self.x
            return self.x
        else:
            return -self.x
    cpdef negY(self,set=False):
        if set == True:
            self.y = -self.y
            return self.y
        else:
            return -self.y
    cpdef posX(self,set=False):
        if set == True:
            self.x = +self.x
            return self.x
        else:
            return +self.x
    cpdef posY(self,set=False):
        if set == True:
            self.y = +self.y
            return self.y
        else:
            return +self.y
    cpdef double powX(self,x:int):
        self.x **= x
        return self.x
    cpdef double powY(self,y:int):
        self.y **= y
        return self.y
    cpdef double truedivX(self,x:int):
        self.x /= x
        return self.x
    cpdef double truedivY(self,y:int):
        self.y /= y
        return self.y
    cpdef bint isX(self,x:int):
        return self.x is x
    cpdef bint isnotX(self,x:int):
        return self.x is not x
    cpdef bint isY(self,y:int):
        return self.y is y
    cpdef bint isnotY(self,y:int):
        return self.y is not y
    cpdef double rshiftX(self,x:int):
        self.x >>= x
        return self.x
    cpdef double lshiftX(self,x:int):
        self.x <<= x
        return self.x
    cpdef double rrshiftX(self,x:int,x2:int):
        self.x >>= x >> x2
        return self.x
    cpdef double rlshiftX(self,x:int,x2:int):
        self.x <<= x >> x2
        return self.x
    cpdef double rshiftY(self,y:int):
        self.y >>= y
        return self.y
    cpdef double lshiftY(self,y:int):
        self.y <<= y
        return self.y
    cpdef double rrshiftY(self,y:int,y2:int):
        self.y >>= y >> y2
        return self.y
    cpdef double rlshiftY(self,y:int,y2:int):
        self.y <<= y >> y2
        return self.y
    #===================================================
    cpdef double addXX(self):
        self.x += self.x
        return self.x
    cpdef double addYY(self):
        self.y += self.y
        return self.y
    cpdef double subXX(self):
        self.x -= self.x
        return self.x
    cpdef double subYY(self):
        self.y -= self.y
        return self.y
    cpdef double xorXX(self):
        self.x ^= self.x
        return self.x
    cpdef double xorYY(self):
        self.y ^= self.y
        return self.y
    cpdef double mulXX(self):
        self.x *= self.x
        return self.x
    cpdef double mulYY(self):
        self.y *= self.y
        return self.y
    cpdef double floordivXX(self):
        self.x //= self.x
        return self.x
    cpdef double floordivYY(self):
        self.y //= self.y
        return self.y
    cpdef double modXX(self):
        self.x %= self.x
        return self.x
    cpdef double modYY(self):
        self.y %= self.y
        return self.y
    cpdef double powXX(self):
        self.x **= self.x
        return self.x
    cpdef double powYY(self):
        self.y **= self.y
        return self.y
    cpdef double truedivXX(self):
        self.x /= self.x
        return self.x
    cpdef double truedivYY(self):
        self.y /= self.y
        return self.y
    cpdef bint XeqY(self):
        return self.x == self.y
    cpdef bint XnqY(self):
        return self.x != self.y
    cpdef double rshiftXX(self):
        self.x >>= self.x
        return self.x
    cpdef double lshiftXX(self):
        self.x <<= self.x
        return self.x
    cpdef double rrshiftXX(self,x:int):
        self.x >>= self.x >> x
        return self.x
    cpdef double rlshiftX(self,x:int):
        self.x <<= self.x >> x
        return self.x
    cpdef double rshiftY(self):
        self.y >>= self.y
        return self.y
    cpdef double lshiftY(self):
        self.y <<= self.y
        return self.y
    cpdef double rrshiftY(self,y:int):
        self.y >>= self.y >> y
        return self.y
    cpdef double rlshiftY(self,y:int):
        self.y <<= self.y >> y
        return self.y
    #=====================================================
    cpdef double addXY(self):
        self.flag = self.x + self.y
        return self.flag
    cpdef double subXY(self):
        self.flag = self.x - self.y
        return self.flag
    cpdef double subYX(self):
        self.flag = self.y - self.x
        return self.flag
    cpdef double xorXY(self):
        self.flag = self.x ^ self.y
        return self.flag
    cpdef double xorYX(self):
        self.flag = self.y ^ self.x
        return self.flag
    cpdef double mulXY(self):
        self.flag = self.x * self.y
        return self.flag
    cpdef double mulYX(self):
        self.flag = self.y * self.x
        return self.flag
    cpdef double floordivXY(self):
        self.flag = self.x // self.y
        return self.flag
    cpdef double floordivYX(self):
        self.flag = self.y // self.x
        return self.flag
    cpdef double modXY(self):
        self.flag = self.x & self.y
        return self.flag
    cpdef double modYX(self):
        self.flag = self.y % self.x
        return self.flag
    cpdef double powXY(self):
        self.flag = self.x ** self.y
        return self.flag
    cpdef double powYX(self):
        self.flag = self.y ** self.x
        return self.flag
    cpdef double truedivXY(self):
        self.flag = self.x / self.y
        return self.x
    cpdef double truedivYX(self):
        self.flag = self.y % self.x
        return self.flag
    cpdef double rshiftXY(self):
        self.flag = self.x >> self.y
        return self.flag
    cpdef double lshiftXY(self):
        self.flag = self.x << self.y
        return self.flag
    cpdef double rrshiftXY(self,x:int):
        self.flag = self.x >> self.y >> x
        return self.flag
    cpdef double rlshiftXY(self,x:int):
        self.flag = self.x << self.y >> x
        return self.flag
    cpdef double rshiftYX(self):
        self.flag = self.y >> self.x
        return self.flag
    cpdef double lshiftYX(self):
        self.flag = self.y << self.x
        return self.flag
    cpdef double rrshiftYX(self,y:int):
        self.flag = self.y >> self.x >> y
        return self.flag
    cpdef double rlshiftYX(self,y:int):
        self.flag = self.y << self.x >> y
        return self.flag
    
    

cpdef long long int Test_BForce(int a,int b,int c,int d,int e,int f):
    cdef float TEST_COMPUTING_SPEED = 2.0
    while True:
        g = stdn.random.randint(e,f+e)
        if (a+b+c+g)==(d+e+f):
            return g


