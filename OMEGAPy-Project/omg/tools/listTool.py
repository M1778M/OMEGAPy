from . import workspace




class ListTools():
    def __init__(self,list):
        self._list = list
    def ToString(self)->str:
        out = ''
        for i in self._list:
            out += str(i)
        return out
    def if_list_in_list(self):
        for i in self._list:
            if type(i) == list:
                return True
        return False
    def if_type_in_list(self,type_:type):
        for i in self._list:
            if type(i) == type_:
                return True
        return False
    def GAItemlist(self):
        GAItem(self._list)
        return GAItem_out()




def ToString(ls:list)->str:
    out = ''
    for i in ls:
        out += str(i)
    return out
 

def if_list_in_list(ls:list):
    for i in ls:
        if type(i) == list:
            return True
    return False

def if_type_in_list(type_:type,ls:list):
    for i in ls:
        if type(i) == type_:
            return True
    return False



def GAItem(ls:list)->list:
    def if_type(ls_):
        for i in ls_:
            if type(i) is list:
                return False
        return True
                
    out = []
    check_again = False
    for i in ls:
        if type(i) != list:
            out.append(i)
        else:
            check_again = True
            for x in i:
                out.append(x)
    for i in out:
        if type(i) != list:
            check_again = False
        else:
            check_again = True
            
    if check_again:
        GAItem(out)
    else:
        
        if not if_type(out):
            GAItem(out)
        workspace.GA_out = out
        return out

def GAItem_out():
    return workspace.GA_out
    
def GAItemlist(ls):
    GAItem(ls)
    return GAItem_out()

def alist():
    return []
def srange(start,end,step=1):
    if start == abs(start):
        for i in range(start,end,step):
            yield i
    if type(start)!=int or type(end)!=int:
        raise TypeError('Invalid Types in use.')
    if step > end:
        yield start
    else:
        eq = start
        yield eq
        while True:
            if eq == 0:
                for i in range(eq+1,end,step):
                    if eq >= end:
                        break
                    yield i
                break
            if eq >= end:
                break
            eq+=step
            yield eq
def tlist_for_each(ls,enum = lambda x:x ):
    out = []
    
    for item in ls:
        out.append(enum(item))
    return ListTools(out)

def list_for_inner(gen):
    out = []
    for i in gen:
        out.append(i)
    return out

def list_for_each(ls,enum = lambda x:x ):
    out = []
    for item in ls:
        out.append(enum(item))
    yield out
