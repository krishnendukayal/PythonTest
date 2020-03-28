#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

#Write a Python program which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

print("Write a Python program which can generate and print a list where the values are square of numbers between 1 and 20 (both included).")

sq_num = [x*x for x in range(1, 21)]
print(sq_num)