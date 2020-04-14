#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a Python script to count the number of vowels in a given input string

print("Write a Python script to count the number of vowels in a given input string\n")
num = input("Enter the number for sum\t")
str_num=str(num)
total=0

for index in str_num:
    total=total+int(index)

print("Sum of input number {} is {}".format(num, total))