from .error_handling import ValueError
from datetime import time as _time, datetime as _datetime

class Date:
    def __init__(self,date_string,o='/',fr='right2left'):
        self._make_date_init (date_string,o,fr)

    def _icheck(self,nums):
        if len (nums) != 2:
            raise ValueError ('length of day\'s and month\'s value must be 2.')
        if nums[0] == '0':
            return int (nums[1])
        return int(nums)
    def from_str (self):
        return self.date_str
    def equal(self,newdate):
        if type(newdate)==str:
            if self.day == Date(newdate).day and self.month == Date(newdate).month and self.year == Date(newdate).year:
                return True
            return False
        elif type(newdate)==Date:
            if self.day == newdate.day and self.month == newdate.month and self.year == newdate.year:
                return True
            return False
        return False
    def _check(self):
        if (self.day > 31 or self.month > 12) or (self.day <= 0 or self.month <= 0):
            raise ValueError ('month or day of date is invalid.')
        return True
    def _make_date_init (self,dts,o,fr):
        if fr == 'right2left' or fr == 'r2l':
            if len (dts.split(o)) == 3:
                dt = dts.split(o)
                self.year  = int(dt[0])
                self.month = self._icheck (dt[1])
                self.day   = self._icheck (dt[2])
                self.date_str = dts
                self._check()
                return True
            else:
                ValueError (f'Cannot handle \'{dts}\' as a date string .')
        elif fr == 'left2right' or fr == 'l2r':
            if len (dts.split(o)) == 3:
                dt = dts.split(o)
                dt.reverse()
                self.year  = int(dt[0])
                self.month = self._icheck (dt[1])
                self.day   = self._icheck (dt[2])
                self.date_str = dts
                self._check()
                return True
        else:
            raise ValueError (f'Cannot handle \'{fr}\' as a date format use (left2right) or (right2left) .')
Time = _time

class Gender:
    genders = {'male':0,'female':1,'unknown':2,'others':3}
    @staticmethod
    def gender_fromcode (code):
        if code == 0:
            return Gender ('male')
        elif code == 1:
            return Gender ('female')
        elif code == 2:
            return Gender ('unknown')
        elif code == 3:
            return Gender ('others')
        elif code in list(Gender.genders.values()):
            return Gender (list(Gender.genders.keys())[list(Gender.genders.values()).index(code)])
        else:
            return Gender ('unknown')
    def __init__(self,gender_str):
        self.gender  = gender_str.lower()
    def is_male(self):
        if self.gender == 'man' or self.gender == 'male' or self.gender == 'men':
            return True
        return False
    def is_female(self):
        if self.gender == 'female' or self.gender == 'woman' or self.gender == 'women':
            return True
        return False
    def is_unknown(self):
        if not self.is_male() and not self.is_female():
            return True
        return False
    def is_others(self):
        if self.gender == 'others':
            return True
        return False
    @staticmethod
    def add_gender(gender_name,gender_calls:list=None):
        Gender.genders[gender_name] = list(Gender.genders.values())[-1]+1
        if gender_calls == None:
            gender_calls = [gender_name.lower()]
        func_ = f"def is_{gender_name}(self):\n\tif self.gender in {gender_calls}:\n\t\treturn True\n\treturn False"
        exec(func_,globals())
        exec(f'_select = is_{gender_name}',globals())
        setattr (Gender,f'is_{gender_name}',_select)
        return True

_Gender_Male    = Gender ('Male')
_Gender_Female  = Gender ('Female')
_Gender_Unknown = Gender ('Unknown')

class DateTime:
    def __init__(self,date,time):
        if not type(date) == Date and not type(time) == Time:
            raise TypeError ('Unknown Type')
        self.date = date
        self.time = time
        self.datetime = date.from_str()+' '+time.strftime('%r')
        self.year = self.date.year
        self.month = self.date.month
        self.day = self.date.day
        self.hour = self.time.hour
        self.minute = self.time.minute
        self.second = self.time.second
    @staticmethod
    def now():
        n = _datetime.now()
        return DateTime(Date(n.strftime('%Y/%m/%d')),Time(n.hour,n.minute,n.second))


class String:...
class Number:...
class Language:...
class Country:...
class Location:...
class geLocation:...
class File:...
class Directory:...
class Path:...
class FileType:...


def new (Type,input):
    return Type(input)

