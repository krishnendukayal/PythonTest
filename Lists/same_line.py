#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

#write a program to print all elements of list in same line  line  L1 = [2,5,3,4,"apple",7,"mango",40]

print("write a program to print all elements of list in same line  line  L1 = [2,5,3,4,'apple',7,'mango',40]")

L1 = [2,5,3,4,"apple",7,"mango",40]

for i in range(len(L1)):
    print(L1[i], end = " ")