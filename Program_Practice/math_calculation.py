#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a Python script to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console
# (n>0).  Example: If the following n is given as input to the program: 5  Then, the output of the program should be: 3.55

print("Write a Python script to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)\n")
num=int(input("please enter the number\t"))
a_list=[]
sum1=0

for i in range(2, num+1):
    a_list.append(1.0/i)

print(a_list)

for j in range(len(a_list)):
    sum1= sum1 + a_list[j]

print("Sum of list is {}\n".format(sum1))