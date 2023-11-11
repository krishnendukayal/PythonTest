#Write a program that keep taking the name as input from the user and keep adding to the list if not already present. It stops when user enter "end"

print("Write a program that keep taking the name as input from the user and keep adding to the list if not already present. It stops when user enter 'end'")

name = []

while True:
    input_name = input("please enter the name\t")
    if input_name == "end" or input_name == "END" or input_name == "End" or input_name == "eNd" or input_name == "enD" or input_name == "ENd" or input_name == "eND" or input_name == "EnD":
        break
    elif input_name not in name:
        name.append(input_name)
    else:
        pass

if len(name) == 0:
    print("You have Empty list")
    print("You have Empty list")
else:
    print("This is the entered name {}".format(name))