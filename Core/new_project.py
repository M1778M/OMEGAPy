from _getcorepath import *
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('path',help='path to project want to create',type=str)
parser.add_argument('-t','--project-type',default='std',help='type of project default=std',choices=['std','cus','res','app','crs'],type=str) # standard custom research application cross-platform
parser.add_argument('-c','--config',default='&STD&',help='defualt configuration')
settings = {
    }
config = {
    }
ok = {"configs":False,"path":False,"args":False}

status = False

def check_args(args)->"changes config and settings variables and configure for new project":...

def check_path(path)->"check path returns bool":...

def check_configs()->"check configs of default configs then add or create customize config file returns bool":...

def create_project(settings,config,path)->"creates project with parsed arguments":...



if __name__ == "__main__":
    args=parser.parse_args()
    check_args(args=args)
    if check_path(args.path) and \
    check_configs(config) and status:
        create_project(settings,config,args.path)

