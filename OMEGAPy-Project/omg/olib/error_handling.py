E = Exception

class ConnectionFaildError(E):
    def __init__(self,msg):
        super().__init__(msg)

class UnknownError(E):
    def __init__(self,msg):
        super().__init__(msg)

class MemoryError(E):
    def __init__(self,msg):
        super().__init__(msg)

class ValueError(E):
    def __init__(self,msg):
        super().__init__(msg)

class TypeError(E):
    def __init__(self,msg):
        super().__init__(msg)

class SyntaxError(E):
    def __init__(self,msg):
        super().__init__(msg)

class ListError(E):
    def __init__(self,msg):
        super().__init__(msg)

class ProcessError(E):
    def __init__(self,msg):
        super().__init__(msg)

class BadError(E):
    def __init__(self,msg):
        super().__init__(msg)

class MagicCodeError(E):
    def __init__(self,msg):
        super().__init__(msg)

class CoreError(E):
    def __init__(self,msg):
        super().__init__(msg)
