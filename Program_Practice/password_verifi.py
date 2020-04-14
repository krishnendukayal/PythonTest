#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

print("This is a password verification program\n")
pw=input("Please enter the password\t")
la=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ua=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
sc=["$", "#", "@"]
nl=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for wd in pw:
    if wd in la:
        pass
    elif wd in ua:
        pass
    elif wd in sc:
        pass
    elif wd not in nl:
        break
        print("This is valid password")
    else:
        print("Please follow the password rule a-z, A-Z, 0-9, $, # and @")
