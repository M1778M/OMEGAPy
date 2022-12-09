from pathlib import Path
from subprocess import getoutput as crun
from argparse import ArgumentParser
from shutil import copy
import shutil
import os
# Static Variables
nothing = lambda :None
main_path = "./src"
main_file = "./src/main.py"
parser=ArgumentParser(prog="OMEGAPyGuiCompiler",description="For Compiling OMEGAPyGuiMod",epilog="Done")
basic_pyc = 'pyinstaller {0} --onedir --clean --noconfirm -i icon.ico --windowed --runtime-tmpdir tmp '
# Main
def CompileWithPyinstaller (mainf,asname):
    def start ():
        print (" Welcome To OGCompiler ")
    def ask_yn(text:str):
        print(text,end=' ')
        ask = input()
        if 'y' in ask.lower():
            return True
        else:
            return False
    def _execute (cmd):
        return crun(cmd)
    def getargs():
        print('Enter more args like \'--target-architecture x86_64\'')
        more_args=input(':')
        basic_pyc+=more_args
    def process (cmd):
        print (f"Processing '{cmd}'")
        print(crun(cmd))
        print('Process Finished.')
    make_file = Path(f'./src/{asname}.py')
    start()
    if ask_yn('do you really wanna continue?'):nothing()
    else:exit()
    print('the basic compiling code is :'+basic_pyc.format('src/'+asname+'.py'))
    if ask_yn('need more arguments?'):getargs()
    else:nothing()
    copy (main_file,str(make_file))
    process (basic_pyc.format('src/'+asname+'.py'))
    if Path('./tmp/build').exists():
        shutil.rmtree('./tmp/')
        os.mkdir('./tmp')
    shutil.move ('./build','./tmp')
    shutil.move (f'./{asname}.spec','tmp')
    shutil.copytree(f'./dist/{asname}','./release',dirs_exist_ok=True)
    shutil.move ('./dist','./tmp')
if __name__ == '__main__':
    parser.add_argument('option',type=str,default=None,choices=['build','compile'])
    parser.add_argument('-n','--name',type=str,default='umegapy')
    args=parser.parse_args()
    if args.option.lower()=='build' or args.option.lower()=='compile':
        CompileWithPyinstaller (main_file,args.name)
