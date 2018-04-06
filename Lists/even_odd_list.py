a = []
list_data=int(input("How many data do you want for list\t"))
for i in range(list_data):
    input_data = int(input("Enter {} data\t".format(i+1)))
    a.append(input_data)

even = []
odd = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

print("Even list is {}\t".format(even))
print("Odd list id {}\t".format(odd))

mul1 = [ x*x for x in even]
print("Multiplication of Even list is {}\t".format(mul1))
mul2 = [y*y for y in odd]
print("Multiplication of Even list is {}\t".format(mul2))