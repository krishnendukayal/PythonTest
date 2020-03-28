#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

print("Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)")

sq_sum = [x*x for x in range(1, 31) if (x <= 5) or (x >= 25)]
print(sq_sum)