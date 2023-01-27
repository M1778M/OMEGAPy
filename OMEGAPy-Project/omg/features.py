from .tools import listTool

_Executable_List = ['Python','XLang']
_ValidFeatures_Id = [1]

class _StdFeature_Control:
    def __init__(self):
        self.variable_declaration = True
        self.set_variable = self.set_var
        self.get_variable = self.get_var
        self.add_func = self.add_function

    def set_var(self,variable_name:str,variable_value):
        setattr(self,variable_name,variable_value)
        return self
    def get_var(self,variable_name:str):
        return getattr(self,variable_name)
    def add_function(self,func_name,func):
        self.set_var(func_name,func)
        return getattr(self,func_name)
    def feature_id_valid(self,feature_id):
        if feature_id in _ValidFeatures_Id:
            return True
        return False
    def feature_executable_valid(self,feature_executable):
        if feature_executable in _Executable_List:
            return True
        return False
    def feature_name_valid(self,feature_name):
        try:
            exec(f'{feature_name} = 0',locals())
            return True
        except:
            return False

class _Feature:
    def __init__(self,feature_name,feature_executable,feature_id,feature_controller):
        self._control = feature_controller
        self._exec = feature_executable
        self._id = feature_id
        self.name = feature_name
        self.validator
    @property
    def validator(self):
        if self._control.feature_id_valid(self._id) and self._control.feature_executable_valid(self._exec) and self._control.feature_name_valid(self.name):
            self.__usable = True
            return self.__usable
        else:
            self.__usable = False
        return self.__usable
    def add_feature_function(self,function_name,function):
        if self.validator:
            self._control.add_func(function_name,function)
            return getattr(self._control,function_name)
    def __getattribute__(self,attr):
        try:
            return getattr(self,attr)
        except:
            return getattr(self._control,attr)
    def __setattribute__(self,attr,value):
        setattr(self._control,attr,value)
        return self
