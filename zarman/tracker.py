import msvcrt
import time
from sys import stdout,stdin
from colorama import Fore,Back,Style,init as _init

_init()


#// Inital Vars
cr  = Fore.RESET
_d  = Fore.WHITE
_dg = Back.BLACK
br  = Back.RESET
_code = '\x1b'
_Text_UnderlineStyle   = _code+'[4m'
_Text_Reset            = _code+'[0m'
_Background_FixColor   = _code+'[7m'
_Code_Compiler         = "OMEGAPyCompilePy"
_IS_END = False
# StaticMethods
def styler(text,ss,se):
    return ss+text+se
class text_spliter:
    def __init__(self):
        self._text    = ''
        self._splited = []
    def add(self,sometext):
        self._splited.append(sometext)
    def __add__(self,other):
        self._splited.append(other)
        return self
    def make(self):
        self._text = ''
        for item in self._splited:
            self._text += str(item)
        return str(self._text)
    def __call__(self):
        return self.make()
    def __repr__(self):
        text=''
        for item in self._splited:
            text += str(item)
        return str(text)
    
def sprint(*args,end=''):
    if len(args) <= 1:
        print(args[0],end=end)
    else:
        for item in args[:-1]:
            print(item,end=end)
        print(args[-1],end=end)
class Key:
    _2STEP_CHARS = [b'\xe0',b'\x00',b'\xc3\xa0']
    ARROW_KEY_UP = b'\xe0H'
    ARROW_KEY_DOWN = b'\xe0P'
    ARROW_KEY_LEFT = b'\xe0K'
    ARROW_KEY_RIGHT = b'\xe0M'
    ENTER = b'\r'
    CTRL_ENTER = b'\n'
    SPACE = b' '
    CTRL_C = b'\x03'
    CTRL_X = b'\x18'
    CTRL_Z = b'\x1a'
    CTRL_V = b'\x16'
    CTRL_T = b'\x14'
    CTRL_S = b'\x13'
    CTRL_Q = b'\x11'
    TAB = b'\t'
    F1 = b'\x00;'
    F2 = b'\x00<'
    F3 = b'\x00='
    F4 = b'\x00>'
    F5 = b'\x00?'
    F6 = b'\x00@'
    F7 = b'\x00A'
    F8 = b'\x00B'
    F9 = b'\x00C'
    F10 = b'\x00D'
    BACKSPACE = b'\x08'
    ESCAPE = b'\x1b'
    INSERT = b'\xe0R'
    DELETE = b'\xe0S'
    HOME = b'\x00G'
    PAGEUP = b'\x00I'
    PAGEDOWN = b'\x00Q'
    END = b'\x00O'
    
    def __init__(self,key:bytes):
        if type(key) != bytes:
            raise TypeError('The type of key should be \'bytes\'')
        if len(key) == 1:
            self.key=key
        elif len(key) == 2 and chr(key[0]).encode() in Key._2STEP_CHARS:
            self.key=key
        else:
            self.key='WRONG KEY'
def is_pressed(key):
    return msvcrt.getch() == key
def wait_until_keyp(key):
    if type(key) == Key:
        if key.key != 'WRONG KEY':
            while True:
                if is_pressed(key.key):
                    return True
        else:
            return False

    elif type(key) == bytes:
        while True:
            if is_pressed(key):
                return True
    elif type(key) == str:
        while True:
            if is_pressed(key.encode()):
                return True
    else:
        raise TypeError(f"{key}->{type(key)}")

class Event:
    def __init__(self):
        self.event_t = 'Event_T'
    def listener(self):
        if wait_until_keyp(Key(b'q')):
            return self.exit_key_event()
    def exit_key_event(self):
        return 'key found'
# Methods

#Example: Thread(target=tracker.loader,args=('LoadingH','','','','',1)).start();time.sleep(10);tracker._IS_END = True
def loader (text,cs=_d,ce=cr,bg=_dg,eg=br,delay=0.1,char='.'):
    global _IS_END
    while True:
        if _IS_END == False:
            sprint(cs+bg+text+(char*1)+ce+eg,end='\r')
            time.sleep(delay)
            sprint(cs+bg+text+(char*2)+ce+eg,end='\r')
            time.sleep(delay)
            sprint(cs+bg+text+(char*3)+ce+eg,end='\r')
            time.sleep(delay)
            sprint(cs+bg+text+(' '*(len(char)*3))+ce+eg,end='\r')
            
        else:
            _IS_END = True
    return True


