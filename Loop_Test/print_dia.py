input_num = int(input("Enter the no of start\t"))
for i in range(input_num):
    for j in range(i):
        print("*", end=" ")
    print("\n")

for i in range(input_num):
    for j in range(input_num - i):
        print("*", end=" ")
    print("\n")