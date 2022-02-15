from omg import etu
from prj import package_manager as pkgm
from prj import project_manager as prjm
import argparse as _argparse
import os
from colorama import init,Fore,Back
init()















#------------------------- Project Call Mod
if __name__ == '__main__':
    print(Back.RED + Fore.BLUE + "OMEGAPy-Project Admin" + Fore.RESET + Back.RESET)
    parser = _argparse.ArgumentParser(prog="OMEGAPy Project",description='Settings Of Project For Make A Program\n\tOMEGAPy Project Setting You Can Set Arguments To Manage Your Project',epilog='OMEGAPy Project Manager')
    
    def addargs():
        parser.add_argument('ProjectFile',metavar='ProjectFile',help='File Main Of Project.')
        parser.add_argument('-i','--install',help='Add And Installing Package For Use In Project',type=str)
        parser.add_argument('-I','--interpret-command',help='Running Command With VirtualEnvironment',type=str)
        parser.add_argument('-R','--remove-pkg',help='Uninstall Package From VirtualEnvironment',type=str)
        parser.add_argument('-r','--run-project',help='Run The Project',type=str)
        parser.add_argument('-E','--encrypt-project',help='Encrypt Your Project',type=str)
        parser.add_argument('-D','--decrypt-project',help='Decrypt Your Project',type=str)
        
    #calling addargs 
    addargs()
    
    #def check():
        #if args.command.upper()=='install'.upper():
            #parser.add_argument('install',help='Add And Installing Package For Use In Project',type=str)
            #print(f"command : \n{args.command}\n\n\n\ninstall : {args.install}")
        #parser.add_argument('runc',help='Running Command With VirtualEnvironment',type=str)
        #parser.add_argument('rmpkg',help='Uninstall Package From VirtualEnvironment',type=str)
        #parser.add_argument('run',help='Run The Project',type=str)
        #parser.add_argument('show',help='Get Arguments (config , ProjectFiles,Packages)',type=str)
    # processing args
    
    args = parser.parse_args()
    def find_venv():
        dirs = os.listdir()
        if 'venv' in dirs:
            return 'venv\\Scripts'
    if args.ProjectFile:
        
        manager = pkgm.manager(find_venv())
        show = prjm.show()
    
        if args.install:
            
            manager.install_pkg(args.install)
    


