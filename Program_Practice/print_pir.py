input_number = int(input("Please enter the list of "))

for i in range(1, input_number+1):
    s = 0
    for j in range(1, i+1 ):
        if i%j==0:
            s = s + j
            if j == i and s == i:
                print("Absolute number {}".format(i))
        else:
            pass


