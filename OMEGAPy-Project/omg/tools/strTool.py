from . import workspace
from . import listTool

def strLoop(string,step,process=lambda x:x ):
    x = step
    out = []
    for i in range(len(string)):
        out.append(process(string[step-1]))
        step += x
    return listTool.ToString(out)