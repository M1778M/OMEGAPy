from msvcrt import *
def active_interpreter():
    import win32clipboard as clipboard
    def read_clipboard():
        clipboard.OpenClipboard()
        data = clipboard.GetClipboardData()
        clipboard.CloseClipboard()
        return data
    valid_chars = b'\n\rqwertyuiop[]asdfghjkl;\'zxcvbnm,./QWERTYUIOP[]ASDFGHJKL:"<>?\\`~1234567890-=_+'
    ctrl_c = b'\x03'
    ctrl_v = b'\x16'
    ctrl_d = b'\x04'
    def clean_buffer():
        print(end='\r')
        print(' '*50)
    def ask_ctrl_d():
        print('\n',end='')
        ans = input('Do you want to exit[Y,n]?')
        if ans == b'Y' or ans == 'y':
            print('Y pressed')
            exit()
        else:
            print('\n')
        
    while 1:
        stack = b''
        print("XLANG/XInter~# ",end='')
        while 1:
            Input = getch()
            if Input == ctrl_c:
                if stack == b'':
                    print()
                    break
                else:
                    stack=b''
                    clean_buffer()
                    print(end='\r')
                    print("XLANG/XInter~# ",end='')
            elif Input == ctrl_d:
                if stack == b'':
                    ask_ctrl_d()
                    break
            elif Input == ctrl_v:
                clipbrd=read_clipboard()
                stack+=clipbrd.encode()
                print(clipbrd,end='')
            elif Input in valid_chars:
                stack+=Input
            else:
                raise ValueError(f"Character Invalid '{Input}'")
active_interpreter()
