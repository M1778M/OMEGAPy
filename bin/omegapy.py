import argparse
import pathlib as pl

def FindPath(path:str):
    return pl.Path(path).absolute()


parser = argparse.ArgumentParser(description="OMEGAPyTool")

parser.add_argument('project_path',metavar='Project',type=str,help='Read OMEGAPyProject And Set Options On It.')

args = parser.parse_args()

print(FindPath(args.project_path))
