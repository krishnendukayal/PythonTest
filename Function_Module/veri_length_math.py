#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

str="Test Start"
str1="End of Test"
print(str.center(100, "*"))
print("This is s program of variable length Mathematics program\n")
print("press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division \nPress 5 for Modular division \nPress 6 for exponential \nPress 7 for Exit")

a=1
while a==1:

    aa=int(input("Enter the Option \t"))
    if aa==1:
        print("Addition program")
        a1=int(input("How  many value you want to add\n"))
        Sum=0
        for i in range(a1):
            a2=int(input("PLease enter the %d"%i," value\t"))
            sum=sum+a2
        print("Thsi is sum of %d"%a1, sum)
    elif aa==2:
        print("Subtraction Program")
    elif aa==3:
        print("multiplication Program")
    elif aa==4:
        print("Division Program")
    elif aa==5:
        print("Modular division Program")
    elif aa==6:
        print("Exponential program")
    elif aa==7:
        print(str1.center(100,"*"))
        break
    else:
        print("Enter correct option")

# def addition_value():