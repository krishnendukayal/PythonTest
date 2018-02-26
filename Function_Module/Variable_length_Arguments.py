#!/usr/bin/python

print("This is the program of veriable length argument\n")
def verlen(arg1, *varilen):
    print("Output of veriable length argument")
    print(arg1)
    for i in varilen:
        print(i)


verlen(12,4,46,85,56,2,3,2)
