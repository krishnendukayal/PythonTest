#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Given 3 int values, a b c, print their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
# Eg: 3,2,3 Output :2
# 1,2,3 Output :6
# 3,3,3, Output :0

num1=int(raw_input("Please enter the 1st numeric value\t"))
num2=int(raw_input("Please enter the 2nd numeric value\t"))
num3=int(raw_input("Please enter the 1st numeric value\t"))


if num1 == num2 and num1 == num3 and num2 == num3:
    print("All value are same {}".format(num1))
elif num1 == num2 and num1 != num3:
    print("Only {} is different".format(num3))
elif num1 == num3 and num1 != num2:
    print("Only {} is different".format(num2))
elif num2 == num3 and num1 != num2:
    print("Only {} is different".format(num1))
else:
    print("Sum of all value {} + {} + {} = {}".format(num1, num2, num3, (num1 + num2 + num3)))

