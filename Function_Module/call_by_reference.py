#!/usr/bin/python

def changeme(list1):
    print("This is original list before change", list1)
    list1[2]=31313113
    print("This is changed list after modify reference value", list1)

list2=[13,464,798713,1,87641,3645]
changeme(list2)
print("This is list after call the function of reference", list2)