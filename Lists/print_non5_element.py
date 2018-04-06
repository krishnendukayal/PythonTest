#Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

print("Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 30 (both included)")

sq_sum = [x*x for x in range(1, 31) if (x >= 5)]
print(sq_sum)