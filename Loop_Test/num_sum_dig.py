#Write a Python script to print the count of digits of a given input integer. Eg : z=1346289, Count= 7

print("Write a Python script to print the count of digits of a given input integer. Eg : z=1346289, Count= 7")

input_number = input("PLease enter the digit to get the sum\t")

lista = list(input_number)

print("Length of digits of {}={} is {}".format(input_number, lista, len(lista)))