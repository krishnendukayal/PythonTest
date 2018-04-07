#Write a Python script to print the sum of digits of a given input integer. Eg : z=134628, Total =24  ie (1+3+4+6+2+8)

print("Write a Python script to print the sum of digits of a given input integer. Eg : z=134628, Total =24  ie (1+3+4+6+2+8)")

input_number = input("PLease enter the digit to get the sum\t")

lista = list(input_number)
suma = 0

for i in range(len(lista)):
    suma = suma + int(lista[i])
print("Sum of digits of {}={} is {}".format(input_number, lista, suma))