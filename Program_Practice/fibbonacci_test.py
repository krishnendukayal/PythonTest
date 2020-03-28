#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

def fibos(value):
    result=[]
    a, b=0,1
    for i in range(value):
        result.append(a)
        a, b = b, a+b
    return result

print("This is a fibonacci program\n")
input_number=int(input("Please enter the number you want to get fibonacci value\t"))

data=fibos(input_number)
print(data)