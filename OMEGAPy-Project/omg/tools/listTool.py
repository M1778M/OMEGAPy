from . import workspace


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