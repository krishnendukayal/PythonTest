print("Write a Python script to print first 10 Fibonacci series")
result = []

input_data = int(input("Please enter the number  you want to Fibonacci\t"))
a, b = 0, 1

for i in range(input_data):
    result.append(a)
    a, b = b, a+ b

print(result)

