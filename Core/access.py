import hashlib
import configparser
import pickle
import json
import pathlib as pt
from path import Path
from pyrsistent import T
from _paths import corepath,OMEGAPyPPath,omgpath


class user():
    class Access():
        def __init__(self,accessmod,accesspassword):
            self.accessmod = accessmod
            self.accesspassword = hashlib.sha256(accesspassword.encode()).hexdigest()
        def _checkpassword(self,password):
            return (True) if hashlib.sha256(password.encode()).hexdigest() == self.accesspassword else False    
    def __init__(self,uname:str,dir_path):
        self.uname = uname
        self.dir_path = dir_path
    def create_new_access(self,ACCESS_DATA):
        self.access = ACCESS_DATA



accessCfgPath = pt.Path(corepath).joinpath('access.ini')

cfg = configparser.ConfigParser()

def write_access(User:user,accessmod,accesspassword):
    User.create_new_access(user.Access(accessmod,accesspassword))
    with open(Path(User.dir_path).joinpath(f'{User.uname}.ax'),'wb') as ufile:
        pickle.dump(User,ufile)
        ufile.close()
    return True

def read_access(accessFilePath:Path):
    with open(accessFilePath,'rb') as afile:
        access_ = pickle.load(afile)
        afile.close()
    return access_

def check_access(readed_access,accessmod,accesspassword):
    if readed_access.access.accessmod == accessmod and readed_access.access._checkpassword(accesspassword):
        return True
    else:
        return False

def start_create_config():
    def check_exist_main_users_directory():
        if not Path(Path(omgpath).joinpath('/.access/root/')).exists() or not Path(Path(omgpath).joinpath('/.access/guest/')).exists():
            return False
        else:
            return True
    if not check_exist_main_users_directory():
        Path(Path(omgpath).joinpath('/.access/root/')).makedirs_p()
        Path(Path(omgpath).joinpath('/.access/guest/')).makedirs_p()
        
    mcon = configparser.ConfigParser()
    mcon['users']['root'] = str(Path(omgpath).joinpath('/.access/root/'))
    mcon['users']['guest'] = str(Path(omgpath).joinpath('/.access/guest/'))
    mcon['config-files'] = str(Path(omgpath).joinpath('/.access/AccessC.json'))
    # will Create this Variables
    # [users]
    # root=
    # guest=
    # [config-files]
    # accessc=
    users_accesses = str(Path(omgpath).joinpath('/.access/AccessC.json'))
    default_start_accesses = {
        "root":{"uname":'root',"access":'ROOT_ACCESS'},
        "guest":{"uname":'guest',"access":'GUEST_ACCESS'}
    }
    with open(users_accesses,'w') as usersacsfp:
        json.dump(default_start_accesses,usersacsfp)
        usersacsfp.close()
    
    uroot = user('root',str(Path(Path(omgpath).joinpath('/.access/root/')).absolute()))
    uguest = user('guest',str(Path(Path(omgpath).joinpath('/.access/guest/')).absolute()))
    write_access(uroot,'ROOT_ACCESS','root')
    write_access(uguest,'GUEST_ACCESS','guest')

    
cfg.read('cfg.ini')

if cfg["omegapy-core-initcode"]['new'] == 'yes':
    start_create_config()
    cfg['omegapy-core-initcode']['new'] = 'no'
    with open('cfg.ini','w') as config_:
        cfg.write(config_)
        config_.close()
else:
    cfg = configparser.ConfigParser()
    cfg.read('access.ini')

 
    
