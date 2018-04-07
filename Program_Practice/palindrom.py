# Write a Python script to check if an input string is a Palindrome

# Procedure 1:

# input_string=raw_input("Please enter a string to check PALINDROME\t")
#
# length_string=len(input_string)
# loop=length_string//2
# cal_len=length_string-1
#
#
# for i in range(loop):
#     if input_string[i]==input_string[cal_len]:
#         if (cal_len-i) == 2 or (cal_len-i) == 1:
#             print("This is pallindrome")
#         else:
#             cal_len = cal_len - 1
#     else:
#         print("This is not palindrome")
#         break

# Procedure:2

input_string=input("Please enter a string to check PALINDROME\t")

reverse_string=reversed(input_string)

if list(input_string) == list(reverse_string):
    print("This is Palindrome")
else:
    print("This is not Palindrome")

