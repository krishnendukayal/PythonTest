print("This is my 1st program")
print("\nPlease use of this program")
print("Print number based on user input")
i_n = int(input("Please enter your number to print\t"))
for i in range(i_n):
    print("Iteration number\t" + str(i))
    new_value = int(i)*int(i)
    print("Multiplication of iteration number\t" + str(new_value))