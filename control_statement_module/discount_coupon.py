#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

print("Welcome to shopping\n0% Discount below 500\n5% Discount below 1000\n10% Discount below 5000\n15% Discount below 10000\n20% Discount above 20000")
purchase_amount=int(input("Please enter the Purchase Amount\t"))

if purchase_amount >500 and purchase_amount<=1000:
   print("You need to pay this amount\t", (purchase_amount - (purchase_amount*5)/100))
elif purchase_amount >1000 and purchase_amount<= 5000:
   print("You need to pay this amount\t", (purchase_amount - (purchase_amount*10)/100))
elif purchase_amount >5000 and purchase_amount<= 10000:
   print("You need to pay this amount\t", (purchase_amount - (purchase_amount*15)/100))
elif purchase_amount >20000:
   print("You need to pay this amount\t", (purchase_amount - (purchase_amount*20)/100))
else:
   print("You need to pay this amount\t", purchase_amount)
