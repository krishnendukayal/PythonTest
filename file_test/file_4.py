#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# f1=open("kris.txt","w")
# f1.write("this is krish")
# f1.flush()
# f1.close()
# f2=open("kris.txt", "r")
# print(f2.read())
# f2.flush()
# f2.close()
#
# # this is for isatty() function
# fo = open("foo.txt", "wb")
# print ("Name of the file: ", fo.name)
#
# ret = fo.isatty()
# print ("Return value : ", ret)
#
# # Close opend file
# fo.close()

# Open a file
# f1=open("foo.txt", "r")
#
# for i in range(5):
#     l1=next(f1)
#     print("Line no in %d and Line is %s" %(i, l1))
#
# f1.close()

#
# f1=open("foo.txt","r")
# for i in range(5):
#     l1=f1.readline()
#     print(l1)
# f1.close()

f1=open("foo.txt","r")
l1=f1.readlines()
print(l1)
f1.close()