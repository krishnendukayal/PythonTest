#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com
words = ["one", "two", "three"]
for x in words:
  print(x, end=",\t")

number = int(input("Please enter the number for while loop, it will print\t"))
i = 1
while i < number:
  print(i)
  i += 1

number1 = int(input("Please enter the number for while loop, it will print\t"))
for i in range(number1):
  print(i)