#!/usr/bin/python

print("This is file program, read data from user and update to a file and print it once it is done\n\n\n")
fo = open("krish.txt", "a")

fo.write(input("\n"))
fo.write("\n")
fo.close()

f1=open("krish.txt","r")
print("position before read", f1.tell())
print(f1.read())
print("position after read", f1.tell())
f1.close()