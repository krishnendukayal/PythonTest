#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

local=0
def lo_glob(arg1, arg2):
    local=arg1+arg2
    print("This is local variable value:\t", local)
    return

lo_glob(50,50)
print("This is local variable data\t", local)