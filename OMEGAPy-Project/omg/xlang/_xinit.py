import sys
from .clib.cext import *

class XObjectsNotDefineError(Exception):
    def __init__(self,msg):super().__init__(msg)
class StackOverFlow(Exception):
    def __init__(self,msg):super().__init__(msg)
def xndef():
    raise XObjectsNotDefineError('')

def xmalloc(size_t):
    return ['\x00']*size_t

define('x_version',0.01)
define('x_stack',sys.getsizeof(sys)*1024)
define('FNC_nr',(b'nonReadableFunctionCall'))
define('VNC',(b'VariableDeclare'))