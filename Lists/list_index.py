l = [12,200,300,34,5]
print("This is the list {}".format(l))
z = int(input("Enter the value\t"))

if z in l:
    print(l.index(z))
else:
    print("Input number is not present in the list")