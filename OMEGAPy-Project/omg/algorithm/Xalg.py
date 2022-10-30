import sys
import pathlib as pl
import pickle
sys.path.append(str(pl.Path(__file__).parent.parent))
try:
    from xlang import xlib
    from xlang import clib as c
except ImportError as err:
    raise ImportError(err)
except Exception as err:
    raise Exception(err)
class AlgorithmCompilerType:...
c.ifndef('X_AlgorithmV').define("X_AlgorithmV",'0.1')
c.ifndef('AlgorithmBase').define("AlgorithmBase",'"OMEGAPy-OpenAlgorithm"')

class CompilerxAlgorithm16(AlgorithmCompilerType):
    def __init__(self,algorithm,on:str):
        if not type(algorithm) == type:
            raise TypeError("Invalid AlgorithmType.")
    def __new__(self,algorithm,on:str):
        if not type(algorithm) == type:
            raise TypeError("Invalid AlgorithmType.")
        pickle.dump(algorithm,open(on,'wb'))
        return True
def loadAlgorithm(path:str):
    return pickle.load(open(path,'rb'))

xAlgorithm16Base = c.struct(algorithmName=str,algorithmCompiler=AlgorithmCompilerType,algorithmAbout=str)



xAlgorithm16 = xAlgorithm16Base()

xAlgorithm16.algorithmName = 'xAlgorithm16';xAlgorithm16.algorithmAbout = "OMEGAPy>omg>algorithm>OMEGAPy-OpenAlgorithm>X_ALG";xAlgorithm16.algorithmCompiler = CompilerxAlgorithm16;

