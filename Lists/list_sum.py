#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

L1 = [[90,60,30],[69,80,79],[89,90,60]]

suma = []

for i in range(len(L1)):
    suma.append(sum(L1[i]))

print("Sum of marks is {}".format(suma))

