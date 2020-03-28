#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

# Write a program that count vowels in the given string using Dictionary

vowels=["a","e","i","o","u","A","E","I","O","U"]
vowel_counts=0
input_string=input("Enter the string to count the vowels\t")
count=[]
for i in input_string:
    if i in vowels:
        vowel_counts = vowel_counts+1
        count.append(i)
    else:
        pass
print("Number of vowel counts is {}".format(vowel_counts))


a={x : input_string.count(x) for x in count}


print(a)