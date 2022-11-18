class MetaVar:
    def __init__(self,value,const=False):
        self.__value = value
        self.__is_const = const
    def change_value(self,newValue):
        if self.__is_const != True:
            self.__value = newValue
            return 1
        else:
            return None
    def get(self):
        return self.__value


class MetaMethod:
    def __init__(self):
        self.__META_METHOD = True
    def _IsMetaMethod(self):
        return self.__META_METHOD

def OpenFile(filepath:str):
    Source = ""
    with open(filepath,'r')as file:
        Source = file.read()
        file.close()
    return Source
