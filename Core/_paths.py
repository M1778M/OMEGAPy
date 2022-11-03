from pathlib import Path

corepath = str(Path(__file__).parent.absolute())

OMEGAPyPPath = Path(corepath).joinpath('../OMEGAPy-Project/')

omgpath = Path(OMEGAPyPPath).joinpath('/omg/')
