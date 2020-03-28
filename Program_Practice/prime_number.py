#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

r=int(input("Enter upper limit: "))
aa=[]
sum=0
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        aa.append(a)

for ii in range(len(aa)):
    sum = sum + aa[ii]

print(sum)

