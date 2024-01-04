#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input("Enter the integr number\t").strip())
    if n%2==0:
        if n>=2 and n<=5:
            print("Not weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Weird")        
    else:
        print("Weird")
