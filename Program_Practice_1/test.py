#!/usr/bin/python
# Author: Krishnendu Kayal
# Email: krishnendu1985@gmail.com

import time

print("This program will take the input number and will print the number and multiplication of the number")
i_n = int(input("Please enter your number to print\t"))
start_time = time.time()
for i in range(i_n):
    print("Iteration number\t" + str(i))
    new_value = int(i) * int(i)
    exp_value = int(i) ** int(i)
    print("Multiplication of iteration number is\t" + str(new_value))
    print("Exponential of iteration number is\t{}".format(str(exp_value)))
    print(f"Time took to execution this iteration\t{time.time()} Seconds")
end_time = time.time()
print("\nTime took to execution this program\t{} Seconds".format(end_time - start_time))
print("End of program")