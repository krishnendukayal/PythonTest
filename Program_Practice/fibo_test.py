#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

def fibos1(value):
    result=[]
    a, b=0,1
    for i in range(value):
        result.append(a)
        a, b = b, a+b
    return result

if __name__== "__main__":
    print("This is a fibonacci program\n")
    input_number1 = int(input("Please enter the number you want to get fibonacci value\t"))
    f=fibos1(input_number1)
    print(f)