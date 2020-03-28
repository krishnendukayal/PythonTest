print("This program will take the input number and will print the number and multiplication of the number")
i_n = int(input("Please enter your number to print\t"))
for i in range(i_n):
    print("Iteration number\t" + str(i))
    new_value = int(i)*int(i)
    print("Multiplication of iteration number\t" + str(new_value))