from ._xinit import xndef,StackOverFlow,xmalloc
from .clib.cext import *
from .clib.stdlib import *
from .clib.stdio import *
#                            ''' BinaryXnonReadable '''
class _swe:
    def __init__(self):self._stack_writer_enum = 0;self._stack_variable_enum=0;self._std_allocation_memorywaiter = BIN.NONETYPED_OBJECT;self._std_allocation_memorywaiter2 = BIN.NONETYPED_OBJECT;self._std_allocation_memorywaiter3 = BIN.NONETYPED_OBJECT;self._std_allocation_memorywaiter4 = BIN.NONETYPED_OBJECT;self._std_variable_declare = xmalloc(98000);self._std_variable_stack = xmalloc(0);
    def _set(self,x):self._stack_writer_enum = x
swe = _swe()
_version = (defined_objects()['x_version'])if(ifdef('x_version').defined)else(0)
_app_stack = xmalloc((defined_objects()['x_stack'])if(ifdef('x_stack').defined)else(1024*1))
FNC_r = None
FNC_nr = (defined_objects()['FNC_nr'])if(ifdef('FNC_nr').defined)else(None);
VCS =  (defined_objects()['VCS'])if(ifdef('VCS').defined)else(None);
define('XLANG_SYNTAX','"OMEGAPy-NoneSpacePynonClassicSyntax"')
class Variable():
    def __init__(self,size_t,value=None):
        if not value:
            self.stack_from = len(swe._std_variable_stack)
            swe._std_variable_stack[self.stack_from:self.stack_from+size_t]=(['\x00']*size_t)
            self.stack_to = (self.stack_from+size_t)
        else:
            self.stack_from = len(swe._std_variable_stack)
            swe._std_variable_stack[self.stack_from:self.stack_from+size_t]=[value]
            self.stack_to = len(swe._std_variable_stack)
#---------------------------------------------------------------------------------- cnv Functions
def _arr2str(arr):
    out='';
    for i in arr:
        out+=str(i);
    return out;
def _intarrsum(arr): return sum(arr);
def _convert2str(bystr):return bystr.tobytes();
def _convert4str(fcnv): return bytearray(fcnv.encode());
#---------------------------------------------------------------------------------
def varcall(vc): return (f"{_version}-[SettedVariable] type:VariableSetting,msg:trueDeclare,isvalid:true,by:XSTDStackWriter")if(vc==VCS)else(f"{_version}-[UnknownSettedVariable] type:VariableSetting,msg:unknownDeclare,isvalid:false,by:XSTDStackWriter");
def fncall(fnt): return (f"{_version}-[CalledFunction] type:nonReadableFunction,msg:trueCall,isvalid:true,by:XSTDStackWriter")if(fnt==FNC_nr)else(f"{_version}-[CalledFunction] type:ReadableFunction,msg:trueCall,isvalid:true,by:XSTDStackWriter");
def xstackwrite(where,_log):  
    try:_app_stack[where] = _log;swe._set(swe._stack_writer_enum+1);
    except IndexError:raise StackOverFlow ('')
    except Exception as err:raise Exception (err)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#------------------------------------------------------------------------
def x_1772408111(byte8):    swe._std_allocation_memorywaiter = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772428111(byte8):    swe._std_allocation_memorywaiter2 = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772438111(byte8):    swe._std_allocation_memorywaiter3 = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772448111(byte8):    swe._std_allocation_memorywaiter4 = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772408110(byte16):    swe._std_allocation_memorywaiter = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772428110(byte16):    swe._std_allocation_memorywaiter2 = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772438110(byte16):    swe._std_allocation_memorywaiter3 = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772448110(byte16):    swe._std_allocation_memorywaiter4 = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772408101(byte24):    swe._std_allocation_memorywaiter = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772428101(byte24):    swe._std_allocation_memorywaiter2 = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772438101(byte24):    swe._std_allocation_memorywaiter3 = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_1772448101(byte24):    swe._std_allocation_memorywaiter4 = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
#-----------------------------------------------------------------------------
def x_2000006001(s,e,o):    swe._std_allocation_memorywaiter[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_2000006011(s,e,o):    swe._std_allocation_memorywaiter2[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_2000006111(s,e,o):    swe._std_allocation_memorywaiter3[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_2000007111(s,e,o):    swe._std_allocation_memorywaiter4[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
#-----------------------------------------------------------------------------------------
def x_0000000007(byte):    swe._std_allocation_memorywaiter = malloc(byte**1);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_0000020007(byte):    swe._std_allocation_memorywaiter2 = malloc(byte**1);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_0000030007(byte):    swe._std_allocation_memorywaiter3 = malloc(byte**1);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_0000040007(byte):    swe._std_allocation_memorywaiter4 = malloc(byte**1);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
#----------------------------------------------------------------------------
def x_3000000001():xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));return swe._std_allocation_memorywaiter
def x_3000000011():xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));return swe._std_allocation_memorywaiter2
def x_3000000111():xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));return swe._std_allocation_memorywaiter3
def x_3000001111():xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));return swe._std_allocation_memorywaiter4
#----------------------------------------------------------------------------
def x_0001000100(bystr):   printf(_convert2str(bystr));xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_0010000015(fcnv):    _convert4str(fcnv);xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));
def x_0000000021(arr):     xstackwrite(swe._stack_writer_enum,fncall(FNC_nr));return _arr2str(arr) 
#---------------------------------------------------------------------------------|
#---------------------------------------------------------------------------------|

#                               """ HumanReadableFNName """
#------------------------------------------------------------------------------------------------------------------------ mainMemAllocation
def sbyte8o1(byte8):swe._std_allocation_memorywaiter = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte8o2(byte8):swe._std_allocation_memorywaiter2 = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte8o3(byte8):swe._std_allocation_memorywaiter3 = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte8o4(byte8):swe._std_allocation_memorywaiter4 = malloc(byte8**8);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte16o1(byte16):swe._std_allocation_memorywaiter = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte16o2(byte16):swe._std_allocation_memorywaiter2 = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte16o3(byte16):swe._std_allocation_memorywaiter3 = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte16o4(byte16):swe._std_allocation_memorywaiter4 = malloc(byte16**16);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte24o1(byte24):swe._std_allocation_memorywaiter = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte24o2(byte24):swe._std_allocation_memorywaiter2 = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte24o3(byte24):swe._std_allocation_memorywaiter3 = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def sbyte24o4(byte24):swe._std_allocation_memorywaiter4 = malloc(byte24**24);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
#------------------------------------------------------------------------------------------------------------------------ mainMemSetter
def owrite(on,s,e,o):
    if on==1 or on==0:swe._std_allocation_memorywaiter[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    elif on==2:swe._std_allocation_memorywaiter2[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    elif on==3:swe._std_allocation_memorywaiter3[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    elif on==4:swe._std_allocation_memorywaiter4[s:e] = o;xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    else: raise NotImplementedError();xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
#------------------------------------------------------------------------------------------------------------------------ StdMemAllocation
def memall(on,byte):
    if on==1 or on==0:swe._std_allocation_memorywaiter=malloc(byte);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    elif on==2:swe._std_allocation_memorywaiter2=malloc(byte);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    elif on==3:swe._std_allocation_memorywaiter3=malloc(byte);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    elif on==4:swe._std_allocation_memorywaiter4=malloc(byte);xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
    else: raise NotImplementedError();xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
#------------------------------------------------------------------------------------------------------------------------StdMemView
def mview(on):
    if on==1 or on==0:xstackwrite(swe._stack_writer_enum,fncall(FNC_r));return swe._std_allocation_memorywaiter;
    elif on==2:xstackwrite(swe._stack_writer_enum,fncall(FNC_r));return swe._std_allocation_memorywaiter2;
    elif on==3:xstackwrite(swe._stack_writer_enum,fncall(FNC_r));return swe._std_allocation_memorywaiter3;
    elif on==4:xstackwrite(swe._stack_writer_enum,fncall(FNC_r));return swe._std_allocation_memorywaiter4;
    else: raise NotImplementedError();xstackwrite(swe._stack_writer_enum,fncall(FNC_r));
def memlookup(on):return mview(on);
def vmemlookup(where,stack=True,declares=False,enum=False,size=False):
    out = {}
    if stack:out['stack'] = swe._std_variable_stack[where];
    if declares:out['declare'] = swe._std_variable_declare[where];
    if enum:out['enum'] = swe._stack_variable_enum;
    if size:out['size'] = sizeof(swe._std_variable_stack[where]);
    return out;
#------------------------------------------------------------------------------------------------------------------------CvnFuncs
def int2str(i): return ((str)(i));
def str2int(s): return ((int)(s));
def arr2str(arr): return _arr2str(arr);
def intarrsum(arr): return _intarrsum(arr);
#-----------------------------------------------------------------------------------------------------------------------VariableFuncs
def declare(Type,Val):
    id = (swe._stack_variable_enum);
    if Type == int or Type == float:
        swe._std_variable_declare[id]=Variable(1,Val)
        swe._stack_variable_enum+=1;
        return id
    elif Type == list or Type == tuple or Type == set:
        swe._std_variable_declare[id]=Variable(len(Val),Val)
        swe._stack_variable_enum+=1;
        return id
    elif Type == str:
        swe._std_variable_declare[id]=Variable(len(Val),Val)
        swe._stack_variable_enum+=1;
        return id
    else:
        swe._std_variable_declare[id]=Variable(Val.__sizeof__(),Val)
        swe._stack_variable_enum+=1;
        return id




    
def execute(source):
    exec(source,globals())
