import etu
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
class Bot():
    __format = """Token = {}
Name = {}
Password = {}
Data = {}"""
    canceled = True
    def __init__(self,name:str,password:str):
        self.BotName = name
        self.__Token = MBT()
        if __checkpass (password) > 2:
            self.___password = password
        elif __checkpass (password) < 2:
            raise EasyPasswordError ('Password Is Easy')
    def save(self,password,data={}):
        if self.CheckPass(password):
            with open(self.BotName+'.bot','w') as f:
                f.write(Bot.__format.format(self.__Token,self.BotName,self.___password,data))
        else:
            raise FalsePasswordError ('False Password!')
    def setPass(self,OldPassword,NewPassword):
        if OldPassword == self.___password:
            if __checkpass (NewPassword) > 2:
                self.___password = NewPassword
            elif __checkpass (NewPassword) < 2:
                raise EasyPasswordError ('Password Is Easy')
        else:
            raise FalsePasswordError ('False Password!')
    def CheckPass(self,password):
        if password == self.___password:
            return True
        else:
            return False
    def GETTKN(self,password):
        if password == self.___password:
            return self.__Token
        else:
            raise FalsePasswordError ('False Password!')
    
