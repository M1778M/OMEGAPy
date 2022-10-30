import re
from . import xlib
from .clib.cext import define,defined_objects,_function



define('Translator_version',0.1)

def funcjoin(funcname,args):
    try:
        exec(f"out = {funcname}({args})",globals())
    except:
        try:
            exec(f"out = xlib.{funcname}({args})",globals())
        except NameError as err:
            raise NameError (err)
        except Exception as err:
            raise Exception(err)
    return out

def getArg(strarg):
    exec(f'args = {strarg}',globals())
    return args

def declare(vn,vt,vv):
    try:
        exec(f'{vn} = {vt}({vv})',globals())
    except:
        exec(f'{vn} = {vt}(xlib.{vv})',globals())
    return xlib.declare(vt,vv)

def pytranslate(source,splitBy=';'):
    source = source.split(splitBy)
    variables = []
    
    def savev(name,id):
        variables.append((name,id))
    
    for line in source:
        if re.match(r'\s*\w+\s*\w*\s*=\s*.*',line):
            varname = re.search(r'\s+\w+\s*=',line).group().strip('=').strip(' ')
            varval = re.search(r'=\s+.+\s*',line).group().strip('=')
            vartype = re.search(r'^\s*\w+\s+',line).group().strip(' ')
            id = declare(varname,vartype,varval)
            savev(varname,id)
        elif re.match(r'\s*\w+\(.*\)\s*',line) and '=' not in line:
            funcname = re.search(r'\s*\w+\(',line).group().strip('(')
            args = getArg(re.search(r'\(.*\)',line).group())
            funcjoin(funcname,args)
        elif re.search(r'\s*\w+\s*=\s*\w+\(.*\)\s*',line):
            varname = re.search(r'\s*\w+\s*',line).group().strip(' ')
            funcname = re.search(r'\s*\w+\s*\(',line).group().strip('(').strip(' ')
            args = re.search(r'\(.*\)',line).group()
            frun = funcjoin(funcname,args)
            exec(f"{varname} = {frun}",globals())
            id = xlib.declare(type(frun),frun)
            savev(varname,frun)
        elif line.isspace():
            pass
        else:
            raise SyntaxError('Invalid Syntax.')
