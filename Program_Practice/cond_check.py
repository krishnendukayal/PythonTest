#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Given 2 ints, a and b, print  True if one of them is 10 or if their sum is 10.

num1=int(input("Please enter the 1st numeric value\t"))
num2=int(input("Please enter the 2nd numeric value\t"))

if num1 ==10 or num2==10 or (num1+num2)==10:
    print("True")
else:
    print("False")



