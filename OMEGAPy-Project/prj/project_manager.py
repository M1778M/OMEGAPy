import sys
import configparser
import pathlib as pt
import hashlib
global configfile
realpath = str(pt.Path(__file__).resolve()).split('\\')
realpath = realpath[:len(realpath)-1]
rlpath = ''
for i in realpath:
    rlpath += i + '\\'
configfile = configparser.ConfigParser()
configfile.read(rlpath+'../core/config.ini')

class ConfigMainSelection(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class ConfigMainCell(Exception):
    def __init__(self,msg):
        super().__init__(msg)


def update():
    with open(rlpath+'../core/config.ini','w') as cf:
        configfile.write(cf)
        cf.close()
    configfile.read('../core/config.ini')


def getConfigInfo()->list:
    return list(configfile['projectinfo'])
def getConfigOmgPath()->str:
    return configfile['projectinfo']['OMEGAPy-Path']
def getConfigFile()->dict:
    return dict(configfile['files'])

def writeConfigOmgPath(omgpath:str):
    configfile['OMEGAPy-Path']['OMEGAPy-Path'] = omgpath

def addFile(filesel:str,filename:str):
    configfile['files'][filesel] = filename
def addSelection(selname:str):
    configfile.add_section(selname)
def addCell(selname,cellname:str,value:str):
    configfile[selname][cellname] = value
def rmSelection(selname:str):
    if selname == 'projectinfo' or selname == 'files' or selname == 'about-project':
        raise ConfigMainSelection("Can't Remove Main Selections!")
    configfile.remove_section(selname)
def rmCell(selname:str,cellname):
    if cellname.lower() == 'OMEGAPy-Path'.lower() or selname == 'about-project':
        raise ConfigMainCell ("Can't Remove Main Cell From Main Selections")
    configfile.remove_option(selname,cellname)

def fag():
    return configfile

def insert_omg_path():
    obj = fag()
    sels = obj.sections()
    cells = []
    for i in sels:
        cells.append(dict(obj[i]))
    save = {}
    sys.path.insert(1,'..\\')
    from core.controler import project_str
    global configfile
    configfile = configparser.ConfigParser()
    configfile.read_string(project_str)
    for i in range(len(sels)):
        try:
            addSelection(sels[i])
        except configparser.DuplicateSectionError:
            pass
        for j in range(len(cells[i])):
            val = list(cells[i].items())[j][1]
            nam = list(cells[i].items())[j][0]
            addCell(sels[i],nam,val)
    return configfile

def passwd():
    return configfile['about-project']['project_password']
def check_password(password:str):
    from subprocess import run


def _decrypt(intn):
    q = (intn^696)
    return chr(q)

def _encrypt(fprj:str):
    o = []
    for i in fprj:
        q = ord(i) ^ 696
        o.append(q)
    return o


def enCryptSource(source):
    l = _encrypt(source)
    o = [chr(i) for i in l]
    return o

def deCryptSource(source):
    o = [_decrypt(ord(i)) for i in source]
    return o

class show():
    def __init__(self):
        self.path = getConfigOmgPath()
    def init(self):
        sys.path.insert(1,self.path)
    def config(self):
        for i in configfile:
            for j in configfile[i]:
                yield (i,j)
    def ProjectFiles(self):
        return dict(configfile['files'])
    