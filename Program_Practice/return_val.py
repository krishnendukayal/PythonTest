#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Given two int values, return their sum. Unless the two values are the same, then print double their sum.

num1=int(raw_input("Please enter the 1st numeric value\t"))
num2=int(raw_input("Please enter the 2nd numeric value\t"))

if num1 == num2:
    print("Both value are same")
    pass
else:
    print("sum of the value {}".format(num1+num2))
    print("duble of the sum is {}".format((num2+num1)*2))


