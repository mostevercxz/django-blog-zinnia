# coding:utf-8
# Usage: python common_func.py
import sys
def warning(*objs):
    print("warning: ", *objs, file=sys.stderr)

def temp_debug():
    import pdb
    pdb.set_trace()

def get_sys_dict(sysname):
    return dict((getattr(sysname, n), n)
            for n in dir(sysname))

def get_sys_list(sysname):
    return '\n'.join(dir(sysname))

# signle file test
if __name__=="__main__":
    import socket
    warning(get_sys_list(socket))
