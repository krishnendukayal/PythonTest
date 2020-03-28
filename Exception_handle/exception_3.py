#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

try:
    f=open("krishnendu1.txt")

except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
else:
    ff = f.read()
    print(ff)
    f.close()
finally:
    print("Finally !!")