from .tracker import *
from threading import Thread
from sys import stdin,stdout,stderr

oldmem = []
memory = []
pointer = -1
mode = 'w'
human_readable_chars = '`1234567890-=   qwertyuiop[]asdfghjkl;\'\\zxcvbnm,./~!@#$%^&*()_+QWERYIOP}{ASDFGHJKL:"||ZXCVBNM<>?'
clear_code = "\033[H\033[J"

def bufwrite(k):
    stdout.buffer.write(k);stdout.buffer.flush()

def test():
    global pointer,memory
    _ = Key(b'NULL')
    flag = 0
    for key in ktracker():
        if key in _._2STEP_CHARS:
            key += read_key()
            if key == _.ARROW_KEY_LEFT:
                bufwrite(_.BACKSPACE)
                continue
            elif key == _.ARROW_KEY_RIGHT:
                flag -= 1
                c=memory[flag]
                bufwrite(c)
                continue

        flag += 1
        memory.append(key)
        
        if key.decode() in human_readable_chars:
            bufwrite(key)
        elif key == _.BACKSPACE:
            stdout.buffer.write(_.BACKSPACE+b' '+_.BACKSPACE);stdout.buffer.flush()
        elif key == _.ENTER:
            bufwrite(b'\n\r')

if __name__ == '__main__':
    test()
