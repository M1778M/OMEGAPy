from threading import Thread as _Thread


def _Pressed(key):
    print(f'Key Pressed ({key}). \nEvent Worked.')
    return True

class Event:
    def __init__(self):
        self._log = []
    def log(self,context):
        self._log.append(context)

class KeyEvent(Event):
    def __init__(self,EventFormat):
        super().__init__()
        import keyboard
        if self.trueFormat(EventFormat):        
            if keyboard.read_key() == EventFormat:
                if _Pressed(EventFormat):
                    pass
            else:
                pass
        else:
            pass
    def trueFormat(self,format):
        if len(format) == 1 and type(format)==str:
            return True
        else:
            return False