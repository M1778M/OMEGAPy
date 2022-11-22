try:
    from configparser import ConfigParser
    import re
    from colorama import Back,Style,Fore,init
    import pathlib
    from importlib import import_module as import_
    import __projc__ as pj
    from shutil import copyfile
except ImportError as err:
    raise ImportError (err)
except Exception:
    raise Exception (err)

self_path = str(pathlib.Path(__file__).parent)+'\\'

init()
global prj_ini
prj_ini = ConfigParser()
prj_ini.read(self_path+'cfg.ini')
def __prj_str():
    with open(self_path+'cfg.ini','r') as f:
        val = f.read()
        f.close()
    return val
prj_str = lambda : __prj_str()


default_str = \
"""[omegapy-core-initcode]
code=rndn
[license]
projectlicense=omegapy-default-license
[about-project]
project_name=nop
project_password=sh
project_country = country
project_location = Path
project_history=dateUtime
project_id=zbotid
project_code=zbotc"""

project_str = \
"""
[license]
projectlicense=omegapy-default-license
[about-project]
project_name=nop
project_password=sh
project_country = country
project_location = Path
project_history=dateUtime
project_id=zbotid
project_code=zbotc"""
#--------------------------------------
default_dict = {
"omegapy-core-initcode" : 
    {
"code" : "rndn"
    },

"license" : 
    {
"projectlicense" : "omegapy-default-license"
    },

"about-project" : 
    {
"project_name" : "nop",
"project_password" : "sh",
"project_history" : "dateUtime",
"project_country" : "country",
"project_location" : "Path",
"project_id" : "zbotid",
"project_code" : "zbotc",
    }
}
#-------------------------------------

class nonSTD:
    def __init__(self):
        self._ = 'For nonStandard Objects'

class STD_CONFIGFILE_NOTFOUND(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def _cleansp(ls):
    out=[]
    for i in ls:
        if i[0]==' ' or i[0]=='\t' or i[-1]==' ' or i[-1]=='\t':
            out.append(i.strip(' ').strip('\t').rstrip(' ').rstrip('\t'))
    for i in ls:
        if ' ' in i or '\t' in i:
            _cleansp(out)
    return out


class stdc:
    def __init__(self):
        self._init_ok()
    def _init_ok(self):
        try:
            self.stdget = ConfigParser()
            self.stdget.read(self_path+'std.ini')
        except:
            raise STD_CONFIGFILE_NOTFOUND('Cannot find std.ini file. Please reinstall OMEGAPy')
    def get_dict(self):
        return dict(self.stdget)
    def get(self):
        return self.stdget
    def get_projects(self):
        return self.stdget['projects']
    def get_projects_info(self):
        return self.stdget['projects-info']
    def pis_exists(self,prjname:str):
        paths = self.get_projects().values()
        for i in paths:
            check = ConfigParser()
            check.read(str(pathlib.Path(i).absolute())+'/core/config.ini')
            if prjname == check['about-project']['project_name']:
                return True
            elif 'nop' == check['about-project']['project_name']:
                if prjname == pathlib.Path(i).name:
                    return True
        return False
    def get_project_byname(self,prjname):
        paths = self.get_projects().values()
        project = None
        for i in paths:
            check = ConfigParser()
            check.read(str(pathlib.Path(i).absolute())+'/core/config.ini')
            if prjname == check['about-project']['project_name']:
                project = i
                break
            elif check['about-project']['project_name'] == 'nop':
                if prjname == pathlib.Path(i).name:
                    project = i
        return project


def reset():
    global prj_ini
    def edit_ini():
        with open('cfg.ini','w') as f:
            prj_ini.write(f)
            f.close()
    prj_ini = ConfigParser()
    prj_ini.read_dict(default_dict)
    edit_ini()
    path = self_path+'..\\'
    copyfile(path+".Core\\main.copy",path+"OMEGAPy-Project\\main.py")
    return 0;

def prj_ini_reset():
    global prj_ini
    prj_ini = ConfigParser()
    prj_ini.read(self_path+'/cfg.ini')
    
def fprint(*args,formatEncode='utf-8',cs:Fore=None,ce=Fore.RESET,e='\n'):
    op = ""
    if cs:
        for item in args:
            print(cs+item+ce,end='')
            op += str(item)
    else:
        for item in args:
            print(item,end='')
            op += str(item)
    print(e,end=e)
    return op.encode(formatEncode)


def eprint(Oerror,Ferror,Terror:str,Merror:str,Cerror:Fore=Fore.RED):
    try:
        def RAISE(o,f,t,m,c=Fore.RED):
            return fprint(f"{o}:{f}->{t} : {m}",cs=c)
        er = RAISE(Ferror,Terror,Merror,Cerror)
        return 1,er
    except Exception as e:
        print(e)
        return 0,None


def TestConfig():
    # flag = 6
    flag = 0
    
    if prj_ini['omegapy-core-initcode']['code']!="rndn":
        flag += 1
    if prj_ini["about-project"]['project_name']!='nop':
        flag += 1
    if prj_ini['about-project']['project_password']!='sh':
        flag += 1
    if prj_ini["about-project"]['project_history']!='dateUtime':
        flag += 1
    if prj_ini['about-project']['project_id']!='zbotid':
        flag += 1
    if prj_ini['about-project']['project_code']!="zbotc" and prj_ini['about-project']['project_code'][0]=='O':
        flag += 1
    if flag == 6:
        return True,
    else:
        return False,flag



def call(cwhat:str,cas:str):
    if cwhat == 'project_edit_form' and cas == 'ask':
        EditConfig.project_edit_form()
    else:
        eprint("function","call","InvalidArgument","Invalid Acsses!")


def Project_Form():
    Test = TestConfig()
    return Test
def Find(arg:str):
    prj_ini_reset()
    try:
        found = re.search(f'{arg} = .+[^\s]',prj_str).group()
        found = found[found.find('=')+1:]
        return found
    except Exception as err:
        eprint("function",'Find','Exception',err)


class shellini():
    def __init__(self):
        self.__log = set()
    def _Test(self):
        myl = ["Windows","Linux","MacOs"]
        self.fprint(myl,title="What Is You'r Favorite os?",e="Choose one os:")
        cmd = self.set_method()
        print(f"Input Of set_method Is:[{cmd}] Type:[{type(cmd)}]")
        fprint(f"Oh Nice os [{myl[int(cmd)]}]",cs=Fore.BLUE)
    def set_method(self,methodt='GET'):
        if methodt.upper() == 'GET':
            cmd = input()
            return cmd
        else:
            error = eprint("class","shellini","InvalidType","Type Of Argument[methodt] In Function self.set_method Is Invalid!")
            self.__log.add(list(error))
    def clear(self):
        from os import system
        from platform import platform
        platform = platform().upper()
        if "LINUX" in platform or "MAC" in platform:
            system('clear')
        elif "WINDOWS" in platform:
            system('cls')
        else:
            eprint("class/function",'shellini/clear','InvalidSystemPlatform','Cant Analize Your SystemPlatform!')
    def fprint(self,args:list,title="Choose One",titlec=Fore.YELLOW,typE='n',c=Fore.GREEN,e=':',ec=Fore.RED,ae='\n'):
        if typE == 'n':
            fprint(title,cs=titlec)
            for i in range(len(args)):
                fprint(f"[{i}]{args[i]}",cs=c)
            print(ae,end='')
            fprint(e,cs=ec,e='')
        else:
            error = eprint("class","shellini","InvalidType","Type Of Arguement[typE] In Function self.fprint Is Invalid!")
            self.__log.add(list(error))


def Edit_License():
    def edit_ini():
        with open(self_path+'cfg.ini','w') as f:
            prj_ini.write(f)
            f.close()
        prj_ini_reset()
    obj = shellini()
    def Edit():
        obj.clear()
        fprint("Enter Your License : ",e='',cs=Fore.RED)
        cmd = obj.set_method()
        prj_ini['license']['projectlicense'] = cmd
        edit_ini()
        fprint("Completed!",cs=Fore.GREEN)
        return True
    obj.clear()
    loyn = ["Yes","No"]
    obj.fprint(loyn,title="Do You Want Edit Your License",e="-> ",ae='\n\n')
    cmd = obj.set_method()
    if loyn[int(cmd)] == 'Yes':
        Edit()
    else:
        return 0

def CheckConfig():
    NTC = []
    if prj_ini['omegapy-core-initcode']['code']=="rndn":
       NTC.append("rndn") 
    if prj_ini["about-project"]['project_name']=='nop':
        NTC.append("project_name")
    if prj_ini['about-project']['project_password']=='sh':
        NTC.append("project_password")
    if prj_ini["about-project"]['project_location']=='Path':
        NTC.append("project_location")
    if prj_ini["about-project"]['project_history']=='dateUtime':
        NTC.append("project_history")
    if prj_ini['about-project']['project_id']=='zbotid':
        NTC.append("project_id")
    if prj_ini['about-project']['project_code']=="zbotc" and prj_ini['about-project']['project_code']=="zbotc":
        NTC.append("project_code")
    if prj_ini['about-project']['project_country']=='country':
        NTC.append('project_country')    
    return NTC

class EditConfig(nonSTD):
    nonStandardFunction = True
    def project_edit_form():
        import __projc__
        def edit_ini():
            with open(self_path+'cfg.ini','w') as f:
                 prj_ini.write(f)
                 f.close()
            prj_ini_reset()
        def vCountry(country:str):
            v = False
            with open(self_path+'countries.list','r') as f:
                countries = f.read()
                f.close()
            countries = countries.split('\n')
            for country_ in countries:
                if country.upper() == country_.upper():
                    v = True
                    break
            return v
        def vPath(path:str):
            if pathlib.Path(path).exists():
                return True
            else:
                return False                     
        def vName(name:str):
            NameValidChars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890_.'
            Nums = '1234567890'
            v=True
            for c in name:
                if c not in NameValidChars:
                    v = False
                    return v
            if name[0] in Nums:
                return False
            return v
        def __checkpass(passwd):
            
            _Space= ' '

            _multychar = '/?@#!~%^&*()_+|}{:"\'-=\\'

            _Alf = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ_.'

            _Alfc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            _All = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'

            securityToken=0
            
            if len(passwd) < 6:
                eprint("function",'__Anonymous','PasswordLenghtError','The Lenght Of Password Is Smaller Than 6! Is Not Secure.')
                return 0
            elif len(passwd) > 10 and len(passwd) < 15:
                securityToken += 1
            elif len(passwd) > 20:
                securityToken += 2
            else:
                securityToken += 1

            if len(passwd) > 12:
                securityToken += 2

            _CharFound = 0
            f = ''
            for i in _All:
                for x in range(len(passwd)):
                    if passwd[x] == i:
                        if passwd[x] == f:
                            _CharFound += 1
                        f = i

            print(_CharFound)
            if _CharFound >= 5:
                eprint("function",'__Anonymous','EasyPassword','The Password _CharFound Is smaller than 5 Password Is Not Secure')
                return 0
            elif _CharFound < 2:
                securityToken += 1
            else:
                securityToken += 0.5

            if ' ' in passwd:
                securityToken += 2
            for i in passwd:
                try:
                    if int(i) == int(i):
                        securityToken += 1
                        break
                except:
                    pass


            for i in range(len(passwd)):
                for c in _multychar:
                    if passwd[i] == c:
                        securityToken += 1

            for i in _Alfc:
                if i in passwd:
                    securityToken += 1
                    break
            return securityToken

        def vPassword(passwd:str):
            score = __checkpass(passwd=passwd)
            if score >= 2:
                return True
            else:
                return False

        def AutoCom(ls:list):
            error = 0
            opl = []
            for n in ls:
                if n == "project_history":
                    v = __projc__.dateUtime()
                    prj_ini['about-project']['project_history'] = v
                    edit_ini()
                elif n == "rndn":
                    v = __projc__.rndn()
                    prj_ini['omegapy-core-initcode']['code'] = v
                    edit_ini()
                elif n == "project_id":
                    v = __projc__.zbotid()
                    prj_ini['about-project']['project_id'] = v
                    edit_ini()
                elif n == "project_code":
                    v = __projc__.zbotc()
                    prj_ini['about-project']['project_code'] = v
                    edit_ini()
                else:
                    opl.append(n)
            return opl
        def EditFormWith(listoc:list=CheckConfig()):
            _flag = 1
            from time import sleep
            while _flag:
                if 'project_code' not in listoc and 'project_id' not in listoc and 'project_history' not in listoc and 'rndn' not in listoc:
                    obj = shellini()
                    obj.clear()
                    obj.fprint(listoc,title="choose config for edit",e='-/:')
                    cmd = obj.set_method()
                    if cmd == 'exit' or cmd == 'quit':
                        _flag = 0
                        break
                    else:
                        founded = listoc[int(cmd)]
                    obj.clear()
                    obj.fprint([listoc[int(cmd)]],title=f'change value',e=f'value from \'{prj_ini["about-project"][founded]}\' change to :')
                    cmd = obj.set_method()
                    prj_ini['about-project'][founded]
                    if cmd.lower() != 'dont change' or cmd.lower() != 'exit' or cmd.lower() != 'quit':
                        if founded == 'project_name':
                            if vName(founded):
                                prj_ini['about-project']['project_name'] = cmd
                                edit_ini()
                            else:
                                eprint("function","EditFormWith","InvalidChar","Can't Use space [' '] and Dash ['-'] In Your ProjectName")
                                sleep(1)
                        elif founded == 'project_password':
                            if vPassword(cmd):
                                prj_ini['about-project']['project_password'] = cmd
                                edit_ini()
                            else:
                                eprint("function","EditFormWith","EasyPassword","Your Password Is Not Secure! Secure Your Password.")
                                sleep(1)
                        elif founded == 'project_country':
                            if vCountry(cmd):
                                prj_ini['about-project']['project_location'] = cmd
                                edit_ini()
                            else:
                                eprint("function","EditFormWith","InvalidCountry","Your Country Is Not Valid!")
                                sleep(1)
                        elif founded == 'project_location':
                            if vPath(cmd):
                                prj_ini['about-project']['project_location'] = cmd
                                edit_ini()
                            else:
                                eprint('function','EditFormWith','InvalidPath',f'Path {cmd} Is Not Valid Path!')
                                sleep(1)
                    else:
                        pass
                else:
                    listoc = AutoCom(listoc)
        if CheckConfig():
            Test = CheckConfig()
            fprint(f"Do You Want Change All Configures or Not Completed Configures [Y=All,n=NotCompleted]?",cs=Fore.GREEN,e='')
            ques = input()
            if 'Y' == ques.upper().strip(' ').rstrip(' '):
                EditFormWith()
            else:
                listoo = list(prj_ini['about-project'])
                listop = []
                obj = shellini()
                obj.clear()
                obj.fprint(listoo,title='add Configure Item',e='Enter Your Chooses example \'project_name, project_password\' split with \',\' -> ',ec=Fore.BLUE)
                cmd = obj.set_method()
                cmd = cmd.split(',')
                cmd = _cleansp(cmd)
                for i in cmd:
                    if prj_ini['about-project'][i]:
                        listop.append(i)
                for i in range(len(listop)):
                    if ' ' in listop[i]:
                        listop[i] = listop[i].strip(' ')
                EditFormWith(listop)
        def ask():
            question = input(Fore.GREEN + "Your project configuration file is done. Do you want to edit it again[Y,n]?"+Fore.RESET)
            if 'y' == question.strip(' ').rstrip(' ') or 'Y' == question.strip(' ').rstrip(' '):
                call("project_edit_form","ask")
            elif 'n' == question.strip(' ').rstrip(' ') or 'N' == question.strip(' ').rstrip(' '):
                print(Fore.YELLOW+Back.GREEN+"The operation was canceled!"+Fore.RESET+Back.RESET)
                return False
            else:
                print(Back.WHITE + Fore.RED + "Invalid Input Please Type Y,y For Continue or N,n For Canceling!"+Fore.RESET+Back.RESET)	

        if Test[0] == True:
            ask()

def main():
    ...
