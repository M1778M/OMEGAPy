import os
import colorama as clr;
import keyboard as kb;
import sys
import re

clr.init();

_welcome = f"Hi there. (^-^)"

print(clr.Fore.YELLOW+_welcome+clr.Fore.RESET)

class cls:
    stdcolor = clr.Fore.GREEN
    help = '''OMEGAPy-Terminal v=0.2 alg=\"NoneSpace-IOX-osHO\"\n
[Command\t|\tDescription\t|\tVersion]
Help \t Shows OMEGAPyTerminal Commands \t 0.2
'''
def tolog(msg):
    print(f'System> {msg}')

def ierror(msg):
    print(clr.Fore.RED+f'{msg}'+clr.Fore.RESET)

l = lambda s:s.lower() # function('l',args=['s:str'],lines=['return s.lower()']).exe()

def checkby(Input:str,by:str):
    if re.match(by,Input):
        return True
    return False

def pyrun(cmd):
    try:
        exec(cmd[cmd.find('run')+4:],globals())
        return ''
    except Exception as err:
        return str(err)+'\n'
def dprj(cmd:str):
    cmd = cmd.split(' ')
    if len(cmd) != 2 and len(cmd) > 2:
        ierror(f"Invalid Argument {cmd[2]}")
    elif len(cmd) != 2 and len(cmd) < 2:
        ierror(f"Need A Path Of(OMG-Project) For Delete It!")
    elif len(cmd) == 2:
        sub.run(f"rmdir /Q/S {cmd}")
    else:
        ierror("UNKNOWN ERROR!")
class run_command():
    def __init__(self,cmd:str):
        if checkby(l(cmd),'^\\s*help\\s*$'):
            print(cls.help)
        elif checkby(l(cmd),'^\s*exit\s*$'):
            exit(0)
        elif checkby(l(cmd),'^\s*run\s+.+$'):
            print(pyrun(cmd),end='')
        elif "dprj" in l(cmd):
            dprj(cmd)
        else:
            os.system(cmd)

while True:
    get_cmd = input(cls.stdcolor+f"{os.getcwd()}"+clr.Fore.RESET+clr.Fore.LIGHTRED_EX+"$ "+clr.Fore.RESET)
    run_command(get_cmd)
    
