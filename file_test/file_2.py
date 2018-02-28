#!/usr/bin/python

print("This is file program, read data from user and update to a file and print it once it is done\n")
fo = open("krish1.txt", "w")

fo.write("This is krishnendu kayal, this is my file programing test")
fo.close()

f1=open("krish1.txt","r")
print("position before read", f1.tell())
print(f1.read())
print("position after read", f1.tell())
f1.seek(0,0)
print(f1.read())
f1.close()