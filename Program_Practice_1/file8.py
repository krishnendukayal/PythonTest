def is_leap(year):
       
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
    
year = int(input("Please Enter the Year to find out the Leap year\t"))
isleap=is_leap(year)
if isleap == True:
    print("This is Leap Year")
else:
    print("This is not a Leap Year")