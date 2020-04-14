#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a program to take a odd number between 1-10 and print as below
# 999999999
#  7777777
#   55555
#    333
#     1
print("Write a program to take a odd number between 1-10 and print as below")
print("999999999")
print(" 7777777 ")
print("  55555  ")
print("   333   ")
print("    1    \n")
number = int(input("Please enter the number for different print\t"))
a=[]
for i in range(number+1):
    if i%2==1:

        a.append(i)

print(a)

for j in range(len(a)):
    for k in range(len(a)-j):
        print(a[len(a)-(j+1)], end=" ")
    print("\n")