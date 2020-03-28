#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a Python program to sum all the items in a dictionary
print("This is a program to sum all the item on the dictionary\nAssume all keys and values are numeric")
dic1={1:10, 2:20}
print("this is 1st dictionary dic1={1:10, 2:20}")
dic2={3:30, 4:40}
print("this is 2nd dictionary dic2={3:30, 4:40}")
dic3={5:50, 6:60}
print("This is 3rd dictionary dic3={5:50, 6:60}")
dic1.update(dic2)
dic1.update(dic3)
print("updated dictionary")
print(dic1)

dic_key=dic1.keys()
print("All keys of the update dictionary")
print(dic_key)

print("Sum of keys of dictionary is")
print(sum(dic_key))
dic_values=dic1.values()
print("All values of all 3 updated dictionary")
print(dic_values)

print("Sum of values of dictionary is")
print(sum(dic_values))