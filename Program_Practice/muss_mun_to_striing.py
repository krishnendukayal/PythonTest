# Write a Python script to count the number of vowels in a given input string

num = raw_input("Enter the number for sum\t")
str_num=str(num)
total=0

for index in str_num:
    total=total+int(index)

print("Sum of input number {} is {}".format(num, total))