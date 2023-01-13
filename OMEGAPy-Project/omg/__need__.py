import pathlib
import time
import hashlib
import json
import os
import sys
import logging
import platform
import urllib3
import colorama
import nt
import pickle
import random
import threading
import importlib
import datetime

Supports = [
    "8BIT_INTEGER_FLOAT"
    ,"4BIT_INTEGER_FLOAT"
    ,"16BIT_INTEGER_FLOAT"
    ,"32BIT_INTEGER"
    ,"64BIT_STDOMG_INTEGER_FLOAT"
    ,"128BIT_STDOMG_CHAR_STR_INTEGER_FLOAT_X"
    ,"32KBYTE_OMFC_IRETURNOBJ_IRETURNFUNCS"
    ,"64KBYTE_OMFC_IRETURNOBJ_IRETURNFUNCS"
    ,"128KBYTE_OMG_P2D_P2DF_P2DC"
    ,"1MGBYTE_OMG_STDFILE_FILEX_ALGORITHM2"
    ,"10MGBYTE_OMG_STDFILE_FILEX_ALGORITHM2"
    ,"50MGBYTE_OMG_STDFILE_FILEX"
    ,"100MGBYTE_OMG_MKX_ALGORITHM5"
    ]

