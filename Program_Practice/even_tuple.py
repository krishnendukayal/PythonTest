#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10) or given range

# given_tuple=(1,2,3,4,5,6,7,8,9,10)
print("Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10) or given range\n")
dummy_list=[]
for i in range(100):
    if i%2==0:
        dummy_list.append(i)
    else:
        pass

print(tuple(dummy_list))
