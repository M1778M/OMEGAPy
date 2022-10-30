from . import stdalg
import random
import uuid
import pickle
import pathlib
import warnings

random.seed(uuid.uuid1(uuid.getnode()).int)

_stdbasecode16 = int(uuid.uuid1(uuid.getnode()).int / random.randint(987654321111,9999999999999))


def _stdmake(algo):
    return {int(uuid.uuid1(uuid.getnode()).int^int(_stdbasecode16)):algo}

def _check_algorithm(algo):
    if stdalg.Algorithm16 in algo.mro():
        return True
    return False

def alg_16_save_algorithm(algorithm,path:str,name:str):
    class PathError(Exception):
        def __init__(self,msg=''):
            super().__init__(msg)
    def savealg(obj,p,n):
        if pathlib.Path(p).is_dir() and pathlib.Path(p).exists():
            make = str(pathlib.Path(p).absolute())+f'\\{n}.algo'
            pickle.dump(obj,open(make,'wb'))
            return True
        return False
    if _check_algorithm(algoritm):
        _algobj = _stdmake(algorithm)
        stdkey = list(_algobj.keys())[0]
        _algobj[stdkey]._stdcode = stdkey^int(_stdbasecode16)
        if not savealg(_algobj,path,name):
            raise PathError('Invalid Path %s' % path)
        return stdkey
    return False

def alg_16_read_algorithm(code:int,path:str,name:str):
    class PathError(Exception):
        def __init__(self,msg=''):
            super().__init__(msg)
    _algobj = pickle.load(open(str(pathlib.Path(path).absolute())+f'\\{name}.algo','rb'))
    
    if not (_algobj[list(_algobj.keys())[0]]._stdcode ^ code) == _stdbasecode16:
        warnings.warn('Cannot Find Standard Base Code of Object Becuase Modules Imported in Other Process. (It\'s Not Secure)',Warning)
    return _algobj[code]


def alg_32_save_algorithm(algorithm,path:str,std_keyalg):
    if type(std_keyalg) == int:
        pass
    elif type(std_keyalg) == str:
        std_keyalg = int(open(std_keyalg,'r').read())
    else:
        return False
    def _32make(alg32):
        _cg32rndKEY = uuid.uuid1(uuid.getnode()).int
        gen = std_keyalg^_cg32rndKEY
        return {'algorithm':alg32,'key':gen}
    def _CheckALGTrue(alg):
        return ((True)if(type(alg)==stdalg.Algorithm32)else(False))
    def _CheckALGPath(path):
        result = [0,0]
        if pathlib.Path(path).is_file():
            if pathlib.Path(path).exists():
                warnings.warn('OVERWRITE-PROBLEM> The Program did OverWrited on AlgorithmFile/ If You Wanna Use Old Algorithm, Old Algoritm Saved By New Name',Warning)
                result[1] = 1
            result[0] = 1
        return tuple(result)
    if not _CheckALGTrue(algorithm):
        return False
    if _CheckALGPath(path)[0] == 0:
        return False
    objected = _32make(algorithm)
    pickle.dump(objected,open(path,'wb'))
    return objected['key']

def alg32checkOK(algorithm,key,std_keyalg:int=None):
    if not std_keyalg:
        std_keyalg = int(open('./std_cg32.ff','r').read())
    if type(algorithm) != stdalg.Algorithm32:
        return False
    if not hasattr(algorithm,'__ok'):
        return False
    return algorithm.__ok(key^std_keyalg)
    
def alg_32_read_algorithm(path:str,key,std_keyalg:str or int):
    if type(std_keyalg) == int:
        pass
    elif type(std_keyalg) == str:
        std_keyalg = int(open(std_keyalg,'r').read())
    else:
        return False
    if not pathlib.Path(path).is_file() or not pathlib.Path(path).exists():
        return False
    _alg32 = pickle.load(open(path,'rb'))
    return _alg32['algorithm']