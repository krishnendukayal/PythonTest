#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

import os
import time

start="Start of Program"
end="End of Program"

print(start.center(100,"*"))

print(time.asctime())
print("This is a program on file system")
time.sleep(5)
print(time.asctime())
print("Create a directory name krish")
os.mkdir("krish")
time.sleep(5)
print(time.asctime())
print("Rename the directory from krish to babau")
os.rename("krish", "babu")
time.sleep(5)
print(time.asctime())
print("Rename back to original name")
os.rename("babu", "krish")
time.sleep(5)
print(time.asctime())
print("Current directory location")
print(os.getcwd())
time.sleep(5)
print(time.asctime())
print("Remove directory")
os.rmdir("krish")

print(end.center(100,"*"))