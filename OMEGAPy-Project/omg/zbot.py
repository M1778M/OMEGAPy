from . import etu
import pathlib as pl

pc = etu.stdn.pickle

__EPE_PIS = 'Password Is Short'
__EPE_CFEP = 'Char Found EasyPassword'

_Space= ' '

_multychar = '/?@#!~%^&*()_+|}{:"\'-=\\'

_Alf = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ_.'

_Alfc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

_All = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'

class EasyPasswordError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class FalsePasswordError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

def __checkpass(passwd):
    
    securityToken=0
    
    if len(passwd) < 6:
        raise EasyPasswordError (__EPE_PIS)
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
    if _CharFound >= 7:
        raise EasyPasswordError (__EPE_CFEP)
    elif _CharFound < 2:
        securityToken += 1
    else:
        securityToken += 0.5
    
    if _Space not in passwd:
        securityToken -= 1
    else:
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

def __makebotToken():
    import random
    op = ''
    l = random.randint(10,99)
    for i in range(l):
        flag = random.randint(0,3)
        if flag == 2:
            _flag = random.randint(0,2)
            if _flag == 2:
                op += str(random.randint(0,99))
            else:
                op += str(random.randint(0,10))
        else:
            op += random.choice(_Alf)
    return op


MBT = __makebotToken
CP = __checkpass
_Bot__checkpass = CP

class WrongPassword(Exception):
        def __init__(self,txt=''):
            super().__init__(txt)
class InvalidSuffixError(Exception):
        def __init__(self,txt=''):
            super().__init__(txt)
class FileExistsError(Exception):
        def __init__(self,txt=''):
            super().__init__(txt)
class BotNotFoundError(Exception):
        def __init__(self,txt=''):
            super().__init__(txt)
class Bot:
    def makingFormatingV0_01(request,path,**Info):
        def read_format(formatedStr):
            return pc.loads(formatedStr)
        if request == 'GET_INFO':
            if pl.Path(path).is_file() and pl.Path(path).exists() and pl.Path(path).suffix == '.zbot':
                bot = read_format(open(str(pl.Path(path).absolute()),'rb'))
                if Info['password'] == bot.bpassword:
                    return bot
                raise WrongPassword('password for this bot is not True')
            else:
                raise BotNotFoundError()
        elif request == 'MAKE_BOT':
            botfs = Info['bot']
            if pl.Path(path).exists():
                raise FileExistsError()
            elif pl.Path(path).suffix != '.zbot':
                raise InvalidSuffixError('use .zbot end of your file name')
            else:
                pc.dump(botfs,open(str(pl.Path(path).absolute()),'wb'))
                return True
        else:
            print('UNSUPPORTED REQUEST FOR THIS VERSION')
            return False
    def __init__(self,bname,bpassword):
        self.access = True if _Bot__checkpass(bpassword) else False
        self.bname = bname
        bpassword = bpassword
    def make(self,path)->bool:
        if self.access:
            newToken = MBT()
            self.btoken = newToken
            pfs = str(pl.Path(path).absolute())
            if Bot.makingFormatingV0_01('MAKE_BOT',pfs,bot=self):
                return True
        else:
            print('MakeBotError[3]: EasyPasswordError recreate Bot with stronger password')
            return False
    def add_data(name:str,data):
        setattr(self,name,data)


def new_bot(name,password):
    return Bot(name,password)
def save_bot(bot:Bot,path:str):
    return bot.make(path)
def addData2Bot(bot:Bot,dname:str,data):
    setattr(bot,name,data)
def read_botFile(path:str,password):
    return Bot.makingFormatingV0_01('GET_INFO',path,Info={'password':password})
