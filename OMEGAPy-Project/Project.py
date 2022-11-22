from prj import package_manager as pkgm
from colorama import init,Fore,Back
from prj import project_manager as prjm
import argparse as _argparse
import pathlib as pl
import os
init()




def just_in(arg):
    import sys
    if arg in sys.argv:
        return True
    return False










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
        dirs = os.listdir(str(pl.Path(__file__).cwd()))
        if 'venv' in dirs:
            return 'venv\\Scripts'
    if args.ProjectFile:
        
        manager = pkgm.manager(find_venv())
        show = prjm.show()
    
        if args.install:
            manager.install_pkg(args.install)
        if args.remove_pkg:
            manager.uninstall_pkg(args.remove_pkg)
        if just_in('-l') or args.listof_pkgs:
            manager.list_pkgs()

    


