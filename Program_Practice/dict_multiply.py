#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a Python program to multiply all the items in a dictionary
print("Write a Python program to multiply all the items in a dictionary\n")
dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

updated_dict={}
dict_keys=dict.keys()
dict_values=dict.values()
k1=1; k2=1
for key in dict_keys:
    k1=k1*key

for vel in dict_values:
    k2=k2*vel

updated_dict={k1:k2}
print("Multiplication of element of dictionary\t")
print(updated_dict)