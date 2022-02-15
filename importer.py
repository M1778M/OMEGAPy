import importlib as imp


class ImportPathError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


def import_path(path:str,name:str):
    try:
        with open(path,'r') as f:
            filec = f.read()
            f.close()
    except:
        raise ImportPathError("Path Or File NOt Found!")
    with open(name+'.py','w') as f:
        f.write(filec)
        f.close()
    re = imp.import_module(name)
    return re
