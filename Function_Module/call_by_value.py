#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

def changeme(list1):
    print("This is original list before change", list1)
    list1=[12,45,78,56,131]
    print("This is changed list after modify reference value", list1)

list2=[13,464,798713,1,87641,3645]
changeme(list2)
print("This is list after call the function of reference", list2)
#ths is new