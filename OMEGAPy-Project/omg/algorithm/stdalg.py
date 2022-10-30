import numpy

class Algorithm16:
    def __init__(self,name:str=None,base:str='UnknownBaseAlgorithm-NSTD',about:str=None):
        self._algorithm_name = name
        self._algorithm_base = base
        self._algorithm_about = about
    def set_name(self,newname:str):
        self._algorithm_name = newname
        return True
    def set_base(self,newbase:str):
        self._algorithm_base = newbase
        return True
    def set_about(self,newabout:str):
        self._algorithm_about = newabout
        return True

class Algorithm32:
    def __init__(self,name:str=None,base:str='UnknownBaseAlgorithm-NSTD',about:str=None):
        self._algorithm_name = name
        self._algorithm_base = base
        self._algorithm_about = about
    def set_name(self,newname:str):
        self._algorithm_name = newname
        return True
    def set_base(self,newbase:str):
        self._algorithm_base = newbase
        return True
    def set_about(self,newabout:str):
        self._algorithm_about = newabout
        return True
    
class IOAlgorithm(Algorithm16):
    def __init__(self,name:str=None,about:str=''):
        super().__init__(name,'IOAlgorithm32-pyapi',about)
    
