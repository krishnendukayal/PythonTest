#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
print("Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.")

a = []
list_data=int(input("How many data do you want for list\t"))
for i in range(list_data):
    input_data = int(input("Enter {} data\t".format(i+1)))
    a.append(input_data)

l = len(a)

if l >= 1 and a[0]==a[l-1]:
    print("True")
else:
    print("False")