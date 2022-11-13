# cython : language_level=3
#OMEGA-PY (MachinLearning, DeepLearning, AI, DataScience, DataAnalyze, EasyProgramming, ProjectTools, FILE) PROJECT
#Name -> OMEGAPY-P2D.omgprj
#About -> work with models and variables with low of value to focus better and make data with high focus
#LICENSE -> OMEGAPY/omg/NoneSpace/Lisences.nsl.open and OMEGAPY/omg/NoneSpace/OMEGAPy-Lisence.nsl

#By M1778
#------------------------------------------OMEGA-PyProject------------------------------------------------

import numpy as np
############  OMEGAPy Modules

try:
    from .error_handling import *
    from . import mem
    from . import etu
    from .etu import function
    from .tools import listTool
except:
    try:
        from .etu import function
        from . import etu
        from . import mem
    except Exception as err:
        raise ImportError(err)

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
        raise ImportError(err)
###############################################################################################
###############################################################################################

############ Globals

global IReturn

###############################################################################################
###############################################################################################
_IReturn = object

def mklist():
    return list()


class NoneSpaceSyntaxError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


def ImPass():
    pass

class IReturnErrors():
    msgCantSupportType = "Can't Support Type '{}' Just Support Type {} "
   
def IsType(objectv,Type,Errorm:Exception,msg:str):
    if type (objectv) is not Type:
        raise Errorm (msg)
    else:
        return True
def IZone(obj:list):
    if type(obj) is not list:
        try:
            obj = obj.__return__()
        except Exception as err:
            raise IReturnTypeError(err)
    def ch(num:int):
        if len(str(num)) == 1:
            if num == 0:
                return zero
            elif num == 1:
                return one
            elif num == 2:
                return two
            elif num == 3:
                return three
            elif num == 4:
                return four
            elif num == 5:
                return five
            elif num == 6:
                return six
            elif num == 7:
                return seven
            elif num == 8:
                return eight
            elif num == 9:
                return nine
            else:
                raise ValueError ('Invalid ValueInt64!')
        else:
            objl = []
            nl = len(str(num))
            for i in range(nl):
                objl.append(ch(int(str(num)[i])))
            return objl
    
    zero = '0000'
    one = '0001'
    two = '0010'
    three = '0011'
    four = '0100'
    five = '0101'
    six = '0110'
    seven = '0111'
    eight = '1000'
    nine = '1001'
    ot = []
    for i in obj:
        fa = ch(i)
        if type(fa) is int:
            ot.append(fa)
        else:
            for j in fa:
                ot.append(j)
    return ot
    

def IReturnList(Ax0:list,kwargs={'key':False,'start':0,'step':1}):
    if type(Ax0) is not list:
        raise IReturnTypeError (IReturnErrors.msgCantSupportType.format(type(Ax0),(list,IReturn)))
    objs = str(Ax0)
    objs = objs.strip('[')
    objs = objs.strip(']')
    exec (f'objr = IReturn({objs},kwargs={kwargs})',globals())
    return objr
    

def delindex(obj:list,indexes:int):
    del obj[indexes]
    return obj

def irtolist(v:_IReturn):
    return list(v.Ax0)

def ISumEqual(obj:list,other:list):
    return sum(obj) == sum(other)
    
def ISumNotEqual(obj:list,other:list):
    return sum(obj) != sum(other)


def IReverse(objz:list):
    try:
        ot = []
        objr = reversed(objz)
        for i in objz:
            ot.append(next(objr))
    except Exception as err:
        raise ValueError(err)
        
    return ot

def objecute(Object:list)->list:
    if type(Object) is not list:
        raise IReturnTypeError (IReturnErrors.msgCantSupportType.format(type(Object),(IReturn,list)))
    objr = []
    try:
        for i in Object:
            objr.append(int(bin(ord(chr(i)))[2:]))
        return objr
    except Exception as err:
        raise IReturnValueError(err)

def reobjecute(binobject:list)->list:
    if type(binobject) is not list:
        raise IReturnTypeError (IReturnErrors.msgCantSupportType.format(type(Object),(IReturn,list)))
    try:
        for i in range(len(binobject)):
            exec(f'objr = []',globals())
            for c in binobject:
                exec(f'objr.append(int(chr(0b{c})))',globals())
                
        return objr
    except Exception as err:
        raise IReturnValueError(err)

class IReturnException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class IReturnValueError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

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

def mkir(Ax0x0):
    obj=IReturn(Ax0x0)
    return obj
def mkirr(Ax0x0):
    obj=mkir(Ax0x0)
    return obj.__return__()

class IReturnAttributeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class IReturnCalculatingError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class IReturnTypeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class IReturnNotReadyError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class IReturnUnknownError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class StdIReturnObj():
    def __init__(self):
        pass
    def  StandardNumbers(self):
        return [0,1,2]
    def CalculateIReturn(self,number,obj):
        objq = IReturn(number).__return__()
        if obj in objq:
            raise IReturnNotReadyError (f'The Function {self.CalculateIReturn.__name__} Is Not Ready For Use')
        else:
            raise IReturnValueError (f'Invalid \'{number}\' Of Object')

class IReturn():
    global IReturn
    StandardReturnBack = {'key':True,'start':0,'step':1}
    StandardPrintBack = {'key':False,'start':0,'step':1}
    StandardReturnBreak = {'key':True,'start':1,'step':1}
    StandardPrintBreak = {'key':False,'start':1,'step':1}
    StandardDemoObject = -1
    StandardFormating = '-'
    StandardQueryReload = std.StandardQueryStart
    def __init__(self,*Ax0,kwargs={'key':False,'start':0,'step':1}):
        from sklearn import base
        self.__learning = base
        self.Ax0 = Ax0
        self.kwargs = kwargs
        self.formating = IReturn.StandardFormating
        self.__rdfocoa()
    def __rdfocoa(self):
        self.__change_object__ = self._setax0
    def __call__(self):
        return self
    def __iter__(self):
        self.len = len(self)
        self.target = 0
        self.objz = self.__return__()
        return self
    def __sum__(self):
        return sum(self)
    def __pointer__(self,point=0):
        for i in range(point):
            yield self.DictReturn()
    def __lt__(self,other):
        if type(other) is not list:
            raise IReturnValueError(f'Can\'t Support Type \'{type(other)}\' Just Support Type "{IReturn,list}"')
        
        if sum(self.__return__()) < sum(other):
            return True
        else:
            return False
    def __floatback__(self,std=False,stdq='[',stdp=']'):
        objz = self.Ax0
        kwargs = self.kwargs
        if kwargs['key']==True:
            exec('ot = []',globals())
            flag=0
            flagf=0
            if std == False:                
                for i in objz:
                    floatf = i
                    for work in range(int(floatf)+1):
                        for i in range(len(objz)):
                            for j in range(0,int(objz[i])+1):
                                flag+=1
                                exec(f'ot.append({float(str(flagf)[:len(str(int(flagf)))+2])})',globals())
                                flagf+=0.1
                    return ot
            else:
                for i in objz:
                    floatf = i
                    for work in range(int(floatf)+1):
                        for i in range(len(objz)):
                            for j in range(0,int(objz[i])+1):
                                flag+=1
                                exec(f'ot.append({flagf})',globals())
                                flagf+=0.1
                    return ot
        else:
            exec('ot = []',globals())
            flag=0
            flagf=0
            if std==False:
                for i in objz:
                    floatf = i
                    for work in range(int(floatf)+1):
                        for i in range(len(objz)):
                            for j in range(0,int(objz[i])+1):
                                flag+=1
                                exec(f'ot.append({float(str(flagf)[:len(str(int(flagf)))+2])})',globals())
                                print(str(stdq),float(str(flagf)[:len(str(int(flagf)))+2]),str(stdp),'\t',end='')
                                flagf+=0.1
                        print()
                return ot
            else:
                for i in objz:
                    floatf = i
                    for work in range(int(floatf)+1):
                        for i in range(len(objz)):
                            for j in range(0,int(objz[i])+1):
                                flag+=1
                                exec(f'ot.append({float(flagf)})',globals())
                                print(str(stdq) , float(flagf) , str(stdp),'\t\t',end='')
                                flagf+=0.1
                        print()
                return ot
    def ch2array(self, accept_sparse=False, *, accept_large_sparse=True, dtype='numeric', order=None, copy=False, force_all_finite=True, ensure_2d=True, allow_nd=False, ensure_min_samples=1, ensure_min_features=1, estimator=None):
        return self.__learning.check_array(self.ToArray().reshape(-1,1),accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator)
    def plot(self,x=[]):
        from matplotlib.pyplot import plot
        return plot(x,self.__return__())
    def __print__(self):
        for i in range(len(self.Ax0)):
            for j in range(int(self.Ax0[i])):
                for it in range(self.kwargs['start'],j,self.kwargs['step']):
                    std.printf(it,'\t')
                std.printf('\n')
            print()
    def ToArray(self):
        return IReturnArray (self)
    def exe(self,file_name,info={'model_name':"Default",'time_reg':str(etu.stdn.datetime.datetime.now()),'data':'action_get'}):
        try:
            formatexe = _IRETURN.MAKE_EXE['FORMAT_ALGORITHM']
            if info['data'] == 'action_get':
                info['data'] = self.__return__()
            else:
                if type(info['data']) != list:
                    return False
            f = open(file_name,'w')
            f.write(formatexe.format(info['model_name'],info['time_reg'],info['data']))
            f.close()
        except Exception as err:
            raise IReturnUnknownError (err)
        return True
    def __exit__(self,type,value,tradeback):
        stdn.time.sleep(0.00000154)
    def __enter__(self):
        return self.__return__()
    def __sum_eq__(self,other):
        return ISumEqual(self,other)
    def __sum_ne__(self,other):
        return ISumNotEqual(self,other)
    def remove(self,item:int,found=1):
        if type(item) is not int:
            raise IReturnValueError('Item Type Invalid! \t Just Support Type \'int\' .')
        flag = 0
        objr = []
        found = abs(found)
        for i in range(len(self)):
            if self.__return__()[i] == item:
                flag += 1
                if flag == found:
                    for j in self[i+1:]:
                        objr.append(j)
                    break
            else:
                objr.append(self[i])
        return objr
    def packlist(self):
        obj = mklist()
        for i in self.Ax0:
            obj.append(list(mkirr(i)))
        return obj
    def __sub__(self,other):
        if type(other) is not list:
            raise IReturnTypeError (f'Invalid Type Of \'{other}\' Just Support Type {IReturn,list}')
        
        
        obj = self.__return__()
        objr = []
        for i in range(len(other)):
            for j in range(len(obj)):
                if other[i] == obj[j]:
                    pass
                else:
                    objr.append(obj[j])
        return objr
    def __hash__(self):
        objr = 0
        for i in self.__return__():
            objr += hash(str(i))
        return objr
    def __next__(self):
        try:
            obj = self.objz[self.target]
        except:
            pass
        if self.target < self.len:
            self.target += 1
            return obj
        else:
            raise StopIteration ()
        
    def __delattr__(self,name):
        return object.__delattr__(self,name)
    def __len__(self):
        v = 0
        for i in self.__return__():
            v += 1
        return v
    def __le__(self,other):
        return sum(self)<=sum(other)
    def __ne__(self,other):
        objq = self.__eq__(other)
        if False in objq:
            return True
        else:
            return False
    def __reduce__(self):
        return (IReturn, self.__return__())
    def __eq__(self,other):
        #if type(other) is not IReturn:
        #    raise IReturnTypeError (f'Type \'{other}\' Is Not Valid')
        if len(self) != len(other):
            raise IReturnValueError(f'Length \'{other}\' Is Not Equal of Length {len(self)}')
        else:
            test1 = self.__return__()
            if type(other) != list and type(other)==IReturn:
                test2 = other.__return__()
            elif type(other) == list:
                test2 = other
            else:
                raise IReturnTypeError (f"Can't Use Type '{type(other)}' Just Allowed Types {IReturn,list}")
            objr = []
            for i in range(len(other)):
                objr.append(test1[i]==test2[i])
            return objr
    def __dir__(self):
        objd = dir(IReturn)
        lr = []
        for i in range(len(objd)):
            if '__' in objd[i]:
                pass
            else:
                lr.append(objd[i])
        return lr
    def __objecutable__(self):
        return objecute(self.__return__())
    def __reobjecutable__(self,objecuted:list):
        return reobjecute(objecuted)
    def objecutable(self):
        return objecute(self.__return__())
    def reobjecutable(self,objecuted:list):
        return reobjecute(objecuted)
    def __format__(self,obj):
        objq = str(self).split(' , ')
        stringo = ''
        for i in objq:
            stringo += f'{i}{self.formating}'
        return str(stringo)[0:len(str(stringo))-1]
    def __str__(self):
        obj = self.__return__()
        relstr = ''
        for i in obj:
            relstr += str(i)
            relstr += ' , ' 
        return str(relstr)[0:len(str(relstr))-3]
    def __setattr__(self,name,value):
        super(IReturn,self).__setattr__(name,value)
    def fix(self,demo=-1):
        if demo == IReturn.StandardDemoObject:
            objr = []
            stdl = 3
            for i in range(len(self.Ax0)):
                for j in range(int(self.Ax0[i])):
                    objr.append(IReturn(j).__return__())

            return objr
        else:
            objr = []
            hobj = []
            ax = self.Ax0
            stdn = 3
            try:
                for i in range(demo):
                    for j in ax:
                        for s in range(stdn):
                            hobj.append(IReturn(j).__return__()[i])
                        objr.append(hobj)
                        stdn += 1
                return objr
            except Exception as err:
                raise IReturnValueError (f'Length Of {demo} Can\'t Calculate For {ax}')
    def QShow(self):
        return QShow(self)
    def ToDataFrame(self):
        from pandas import DataFrame
        objr = []
        
        for i in range(len(self.Ax0)):
            objr.append(IReturn(self.Ax0[i]).__return__())
        
        return DataFrame(objr)
    def ToSeries(self):
        from pandas import Series
        return Series(self.__return__())
    def big(self,demo=1):
        objr = []
        hobj = []
        ax = self.Ax0
        stdn = 3
        try:
            for i in range(demo):
                for j in ax:
                    for s in range(stdn):
                        hobj.append(IReturn(j).__return__())
                    objr.append(hobj)
                    stdn += 1
            return objr
        except Exception as err:
            raise IReturnUnknownError (err)
    def DictReturn(self,copy:list=None):
        if copy is not None:            
            objl = len(self.__return__())
            ot = {}
            for i in range(objl):
                ot[copy[i]] = self[i]
            return ot
        else:
            objl = len(self.__return__())
            ot = {}
            for i in range(objl):
                ot[i] = self[i]
            return ot
    def __getattribute__(self,attr):
        return super(IReturn,self).__getattribute__(attr)
    def __getattr__(self,attr):
        raise IReturnCalculatingError(f"IReturn Object Can't Calculate attribute '{attr}' ")
    def __getitem__(self,other):
        return self.__return__()[other]
    def add_obj(self,Object:object):
        try:
            obj = self.__return__()
            obj.append(Object)
            #self = obj
            return obj
        except Exception as err:
            raise IReturnValueError(err)
    def plus(self,objp):
        try:
            return IPlus(self,objp)
        except:
            return IPlus(self,[objp])
    def add(self,objp):
        try:
            return Plus(self,objp)
        except:
            return Plus(self,[objp])
    def dindex(self,index:int):
        obj = irtolist(self)
        ret = delindex(obj,index)
        self._setax0(ret)
        return True
    def rpop(self):
        self.Ax0 = self.Ax0[:len(self.Ax0)-1]
        return True
    def radd(self,objfa:list or tuple or set):
        try:
            save = self.Ax0
            try:
                save += tuple(objfa)
                self.Ax0 = save
                return True
            except:
                for i in objfa:
                    save += (i,)
                self.Ax0 = save
                return True
        except Exception as err:
            raise IReturnTypeError(err)
    def __add__(self,other:list):    
        return self.add(other)
    def reverse(self):
        objz = list(self.Ax0)
        objr = IReverse(objz)
        objR = IReturnList(objr)
        return objR
    @property
    def obj(self):
        return self.Ax0
    def _setax0(self,ofa:list or tuple or set):
        self.Ax0 = tuple(ofa)
        return True
    def clear(self):
        self.Ax0 = (0,0,0)
        return []
    @property
    def zone(self):
        obj = self.Ax0
        objl = list(obj)
        objR = IReturnList(objl,kwargs=IReturn.StandardReturnBack)
        return IZone(objR)
        
    def ToString(self):
        return str(self)
    def __return__(self):
        ot = []

        for i in range(len(self.Ax0)):
            for j in range(int(self.Ax0[i])):
                for it in range(self.kwargs['start'],j,self.kwargs['step']):
                    ot.append(it)

        return ot
    def __repr__(self):

        if self.kwargs['key']==True:
            ot = []
            for i in range(len(self.Ax0)):
                for j in range(int(self.Ax0[i])):
                    for it in range(self.kwargs['start'],j,self.kwargs['step']):
                        ot.append(it)

            return str(ot)
        else:
            for i in range(len(self.Ax0)):
                for j in range(int(self.Ax0[i])):
                    for it in range(self.kwargs['start'],j,self.kwargs['step']):
                        std.printf(it,'\t')
                    std.printf('\n')
            print()

            return str(self.__return__())


def IArray(arr:np.ndarray,kwargs=IReturn.StandardPrintBack):
    if type(arr) is not np.ndarray:
        raise IReturnValueError ('Invalid Array!')
    obja = list(arr)
    objl = []
    for i in obja:
        if type(i) is not int:
            if type(i) is list:
                for j in i:
                    objl.append(j)
            else:
                for c in obja:
                    if type(c) is not int:
                        if type(c) is list:
                            for e in c:
                                objl.append(e)
                        else:
                            objl.append(c)
                    else:
                        objl.append(c)
        else:
            objl.append(i)
    
    return IReturnList(objl)



def setc(bin:Vbin):
    IsType(bin,Vbin,IReturnTypeError,f'Invalid Type [{type(bin)}]')
    obj = etu.user.login(username='root',passwd=std.password)
    obj.createXfile(name='.bof',passname='BinaryOmegaFile')
    file = obj.findFile(name='.bof.BinaryOmegaFile')
    file.overWrite(std.StandardWriteEO.format('etu.Vbin','Node.w.setc','NoneSpaceWorkingPage')+f'BinCode[{bin}]')
    file.fclose()
    
    
def IPrint(objz:IReturn):
    for i in range(len(objz.Ax0)):
        for j in range(int(objz.Ax0[i])):
            for it in range(objz.kwargs['start'],j,objz.kwargs['step']):
                std.printf(it,'\t')
            std.printf('\n')
        print()
    


def Iabs(objz:IReturn)->list:
    try:
        objr = []
        for i in objz:
            objr.append(abs(i))
    except Exception as err:
        raise IReturnTypeError (err)
    return objr

def IReturnArray(objz:IReturn):
    if type(objz) is not IReturn:
        raise IReturnTypeError (f'Invalid Type "{type(objz)} IReturn.__objecute__:Typer"')
    objr = objz.__return__()
    
    return np.array(objr)
def IRange (start=0,end:int=None,step=1):
    if not end:
        raise IReturnValueError (f'can\'t Calculate Object {end}')
    exec ('objr = []',globals())
    for i in range(start,end,step):
        exec(f'objr.append({IReturn(i).__return__()})',globals())        
    return objr


def Plus(obj,objz:list,kwargs=IReturn.StandardReturnBack):
    try:
        exec ('objre = []',globals())
        objr = list(objz)
        objr_ = list(obj)
        objr = str(objr).strip('[').strip(']')
        objr_ = str(objr_).strip('[').strip(']')
        exec (f'objre = [{objr_},{objr}]',globals())
        return objre
    except Exception as err:
        raise IReturnUnknownError (err)



def IPlus(obj,objz:list,kwargs=IReturn.StandardReturnBack):
    try:
        exec ('objre = []',globals())
        objr = list(objz)
        objr_ = list(obj)
        objr = str(objr).strip('[').strip(']')
        objr_ = str(objr_).strip('[').strip(']')
        exec (f'objre = [{objr_},{objr}]',globals())
        return IReturnList(objre)
    except Exception as err:
        raise IReturnUnknownError (err)

def IRefloat(objz:list,std=False,stdq='[',stdp=']',kwargs=IReturn.StandardPrintBack):
    if type(objz) is not list:
        raise IReturnTypeError (IReturnErrors.msgCantSupportType.format(type(Ax0),(list,IReturn)))
    objz = str(objz)
    objz = objz.strip('[')
    objz = objz.strip(']')
    exec (f'objr = IReturn({objz},kwargs={kwargs}).__floatback__({std},\'{stdq}\',\'{stdp}\')',globals())
    return objr
    
    
        
class IRand():
    global random
    def __init__(self):
        import random
        self.rand = random
    def RandReturn(length:int,_from=0,_to=10):
        import random as rand
        if length <= 0:
            raise IReturnValueError ('length Invalid -> use (length < 0)')
        objl = []
        for i in range(length):
            objl.append(rand.randint(_from,_to))
        return IReturnList(objl)
    def RandFloat(length:int,_from=0,_to=1,std=False,stdq='[',stdp=']',kwargs=IReturn.StandardPrintBack):
        import random as rand
        if length <= 0:
            raise IReturnValueError ('length Invalid -> use (length < 0)')
        objl = []
        for i in range(length):
            objl.append(rand.uniform(_from,_to))
        return IRefloat(objl,std=std,stdq=stdq,stdp=stdp,kwargs=kwargs)
    def normal(length=1,overend=2):
        exec('flg = []',globals())
        try:
            for i in range(int(length)):
                exec (f'flg.append({np.random.normal(overend)})',globals())
            return IRefloat(flg)
        except Exception as err:
            raise IReturnValueError (err)






class QShow():
    def __init__(self,obj:IReturn):
        if type(obj) is not IReturn:
            raise IReturnTypeError(IReturnErrors.msgCantSupportType.format(type(obj),IReturn))
        from colorama import Fore,Back,init,Style,initialise
        from pandas import DataFrame
        from numpy import nan
        import matplotlib.pyplot as plt
        from subprocess import getoutput as com
        self.com = com
        self.plt = plt
        self.__NaN = nan
        self.__Fore = Fore
        self.__Back = Back
        self.__init = init
        self.__Style = Style
        self.initialise = initialise
        self.__ir = obj
        self._spaces = ' '
        self._linec = '|'
        self.__df = self.__ir.ToDataFrame()
    def QClear(self):
        print(self.com('clear'))
        return None
    def hub(self,objl=0,objr=0,echo='->',start='',end='\n',step='\t',title='QShow'):
        print(title,'\n',start,end='')
        for i in range(len(self.__ir)):
            for j in range(objl):
                print(echo,step,end='')
                for c in range(objr):
                    print(self.__ir[i])
            print(end,end='')
    def plot(self):
        self.plt.style.use('dark_background')
        return self.plt.plot(self.__ir.__return__())
    def show(self):
        return self.plt.show()
    def __format__(self,obj):
        objq = self.__repr__()
        return str(objq)
    def __repr__(self):
        self.__init()
        exec('ot = []',globals())
        objrs = str(self.__ir).split(',')
        objr = ''
        for i in range(len(objrs)):
            objr += self.__Fore.CYAN + self._linec + self._spaces + self.__Fore.RED + str(objrs[i]) + ' ' 
        objr += self.__Fore.CYAN + self._linec + self.__Fore.RESET
        return objr


class OperationError(Exception):
    def __init__(self,msg):
        super().__init__(msg)



def remove_quotes(string):
    out = ''
    for i in range(len(string)):
        if string[i] == '\'' or string[i] == '"':
            continue
        out+=string[i]
    return out

def _zadd(*Xx):
    return sum(Xx)
def mul(*Xx):
    temp = 0
    temp2 = 1
    for x in listTool.list_for_inner(Xx):
        temp2=x*temp2
        temp += temp2
    return temp
def _zdiv(*Xx):
    return Xx[0]/Xx[1]
def _zsub(*Xx):            
    temp=Xx[0]
    for x in listTool.list_for_inner(Xx[1:]):
        temp = temp-x
    return temp
def _zpow(*Xx):
    temp=Xx[0]
    for x in listTool.list_for_inner(Xx[1:]):
        temp = temp**x
    return temp
def _zmod(*Xx):
    temp=Xx[0]
    for x in listTool.list_for_inner(Xx[1:]):
        temp = temp%x
    return temp
def _zNum(*args):
    if type(args[0])==list:
        return len(args[0])
    else:
        return len(args)


class ExL(): # ExtraLevels
    def __init__(self,max:int,operation='Lx(xx,..)->add(x.)/(Num(x.)*Num(Le))',min=2,input_go=2,linearModel=False):
        self._OPR = operation
        self._max = max
        self._min = min
        self._inpg = input_go
        self._lm = linearModel
        self._startfrom = 1
        self._LEVELS = []
    def get_values(self):
        return (self._max,self._min,self._inpg)
    
    def fm(self,opr,xn):

        STD_FORMATS = ['Lx(xx,..)']
        STD_FUNCS = ['Lx','Num','Len','add','sub','div','mul','pow','mod']
        STD_VARS = ['x','xx','x.','Le']
        FUNCS_DE = ['(',')']
        MATH_OP = ['+','-','*','**','/','%']
        SPLIT = '->'
        if opr.split('->')[0] not in STD_FORMATS:
            raise OperationError(f"Operation '{opr}' is not valid")
        OP = opr.split('->')[1]
        main = OP
        xx = ['x{0}']*xn
        r = 1
        for x in range(len(xx)):
            xx[x] = xx[x].format(r)
            r+=1
        xex = ''
        for x in range(len(xx)):
            if x == xn-1:
                xex+='{'+str(xx[x])+'}'
            else:
                xex+='{'+str(xx[x])+'}'+', '
        
        main=main.replace('add','_zadd')
        main=main.replace('div','_zdiv')
        main=main.replace('mod','_zmod')
        main=main.replace('pow','_zpow')
        main=main.replace('sub','_zsub')
        main=main.replace('mul','_zmul')
        main=main.replace('Num','_zNum')
        main=main.replace('Le','_zLe')
        
        main=main.replace('x.',xex)
        
        ys = ['y{0}']*(xn*self._inpg-xn+1)
        r = 1
        for x in range(len(ys)):
            ys[x] = ys[x].format(r)
        yey = ''
        for x in range(len(ys)):
            if x == xn-1:
                yey+=str(ys[x])
            else:
                yey+=str(ys[x])+', '
        outputs = yey
        
        return (main,xex,outputs,ys)
    def make_operation(self,opr,max,min,inpg):
        _zLe=[0]*((min*inpg)+max)
        FLEVEL = 0
        AN = min
        AN_ni = 1
        AN_l = set()
        for _ in range(max):
            FLEVEL+=1
            if FLEVEL > max:
                break
            AN_o = ['']*FLEVEL
            for x in listTool.list_for_each(AN_o,lambda x:x.join(f'x{AN_ni}')):
                AN_l.add(x[0])
                AN_ni += 1
            calcedfm = self.fm(self._OPR,FLEVEL)
            #Level = function('_EXL_LVLC',AN_l,{'_zLe':_zLe},[f"exec(f'y = {self.fm(opr,FLEVEL)[0]}',globals())",'return y'])
            Level = f'''
def _EXL_LVLC({remove_quotes(str(tuple(AN_l)).strip('(').strip(')'))}):
    global _zLe
    _zLe = {_zLe}
    for x in range({FLEVEL}):
        exec(f'global _zLe\\ny = {calcedfm[0]}',globals())
    return y'''
            exec(Level,globals())
            print(Level)
            setattr(self,f'LEVEL{FLEVEL}',_EXL_LVLC)
            self._LEVELS.append(_EXL_LVLC)
    def learn_operation(self):
        self._create_functions()
    def learn(self):
        self.learn_operation()
        
    def _input_from(self,input,frm=None,to=-1):
        if frm == None:
            frm = 1
        if to == -1:
            to = self._max
        levels = self._LEVELS
        levels.reverse()
        
        
    def _create_functions(self):
        self._LEVELS=[]
        max,min,inpg = self.get_values()
        self.make_operation(self._OPR,max,min,inpg)
        




















