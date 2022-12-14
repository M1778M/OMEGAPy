from prj import package_manager as pkgm
from colorama import init,Fore,Back
from prj import project_manager as prjm
import argparse as _argparse
import pathlib as pl
import os
import sys
init()



def print_error(errT,errMsg):
    print (Fore.RED,errT+': ',Fore.RESET,errMsg)

def just_in(arg):
    import sys
    if arg in sys.argv:
        return True
    return False
def print_info(infotxt:str):
    print (Fore.GREEN+'['+Fore.RESET+'*'+Fore.GREEN+'] '+Fore.RESET+infotxt)
def raise_error (error_t,error_msg,code):
    if code == 0:
        print_error (error_t,error_msg)
        sys.exit()
    elif code == 1:
        print_error (error_t,error_msg)
    else:
        raise_error(error_t,error_msg,0)









#------------------------- Project Call Mod
if __name__ == '__main__':
    print(Back.RED + Fore.BLUE + "OMEGAPy-Project Admin" + Fore.RESET + Back.RESET)
    parser = _argparse.ArgumentParser(prog="OMEGAPy Project",description='Settings Of Project For Make A Program\n\tOMEGAPy Project Setting You Can Set Arguments To Manage Your Project',epilog='OMEGAPy Project Manager')
    
    def addargs():
        parser.add_argument('ProjectFile',metavar='ProjectFile',help=Fore.CYAN+'Main File Of Project.'+Fore.RESET)
        parser.add_argument('-i','--install',help=Fore.GREEN+'Add And Installing Package For Use In Project'+Fore.RESET,type=str)
        parser.add_argument('-I','--v-interactive',help=Fore.GREEN+'Running Command With VirtualEnvironment'+Fore.RESET,type=str)
        parser.add_argument('-R','--remove-pkg',help=Fore.GREEN+'Uninstall Package From VirtualEnvironment'+Fore.RESET,type=str)
        parser.add_argument('-r','--run-project',help=Fore.GREEN+'Run The Project'+Fore.RESET,type=str)
        parser.add_argument('-E','--encrypt-project',help=Fore.GREEN+'Encrypt Your Project'+Fore.RESET,type=str)
        parser.add_argument('-D','--decrypt-project',help=Fore.GREEN+'Decrypt Your Project'+Fore.RESET,type=str)
        parser.add_argument('-l','--listof_pkgs',help=Fore.GREEN+"Show List Of Packages Installed"+Fore.RESET)
    #calling addargs 
    addargs()
    
    
    args = parser.parse_args()
    def find_venv():
        if Path('./venv').exists() or Path('./.venv').exists() or Path('./env').exists() or Path('./.env').exists():
            get = [Path('./venv').exists() , Path('./.venv').exists() , Path('./env').exists() , Path('./.env').exists()]
            for i in range(len(get)):
                if get[i] == True:
                    if i == 0:
                        return Path('./venv/Scripts')
                    elif i == 1:
                        return Path('./.venv/Scripts')
                    elif i == 2:
                        return Path('./env/Scripts')
                    elif i == 3:
                        return Path('./.env/Scripts')
                    else:
                        continue
            return False
                    
        else:
            raise_error ("EnvironmentNotFoundError","Cannot find Environment",1)
            print_info("Using system python installed.")
            return 3

    if args.ProjectFile:
        
        manager = pkgm.manager(find_venv())
        show = prjm.show()
    
        if args.install:
            manager.install_pkg(args.install)
        if args.remove_pkg:
            manager.uninstall_pkg(args.remove_pkg)
        if just_in('-l') or args.listof_pkgs:
            manager.list_pkgs()

    


