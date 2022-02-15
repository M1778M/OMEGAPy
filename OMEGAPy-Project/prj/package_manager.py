import os

class ConfigInvalidItemError(Exception):
    def __init__(self,msg):super().__init__()

def auto_vpath():
    import configparser
    cp = configparser.ConfigParser()
    cp.read('../core/config.ini')
    try:
        return cp['venv']['path']
    except Exception as err:
        raise

class manager():
    def __init__(self,venvpath:str):
            self.vpath = venvpath
            self.py = f"{self.vpath}\\python.exe -m "
    def pym(self,cmd):
        os.system(self.py + cmd)
    def install_pkg(self,pkgname:str):
        self.pym(f'pip install {pkgname}')
    def uninstall_pkg(self,pkgname:str):
        self.pym(f'pip uninstall {pkgname}')
    def list_pkgs(self):
        self.pym('pip list')
    def run_(self,cmd):
        self.pym(cmd)