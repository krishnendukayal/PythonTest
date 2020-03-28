#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

print("This is a printing star program")
num=int(input("Please input the number you want to use for star print\t"))
for i in range(num):
    for j in range(i):
        print("*", end=" ")
    print("\n")