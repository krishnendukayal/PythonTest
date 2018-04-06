a = []
list_data=int(input("How many data do you want for list\t"))
for i in range(list_data):
    input_data = int(input("Enter {} data\t".format(i+1)))
    a.append(input_data)

print("Here is the list {}".format(a))
sum = 0
mul = 1

for j in range(1, input_data+1):
    sum = sum + j

print("Sum of list {} is {}".format(a, sum))


for k in range(1, input_data+1):
    mul = mul * k

print("Sum of list {} is {}".format(a, mul))