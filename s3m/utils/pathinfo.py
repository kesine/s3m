
import os

def src_dir():
    return os.path.dirname(os.path.realpath(__file__))

def code_dir():
    return os.path.dirname(src_dir())

def log_dir():
    return code_dir()+'/log'

def conf_dir():
    return code_dir()+'/conf'
	