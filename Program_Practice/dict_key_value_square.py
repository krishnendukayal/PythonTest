#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a Python program which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
print("Write a Python program which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys\n")
emply_dict={}
for index in range(1, 21):
    update_dic={index : index*index}
    emply_dict.update(update_dic)

print(emply_dict)
print(emply_dict.keys())
print(emply_dict.values())