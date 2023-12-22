def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return



def example():
   print("This is another program\nCalling other function")
   greetings()
   return

example()


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")



def add(a):
   print(id(a))
   return
a=100
add(a)
print(id(a))




def testfunction(arg):
   print ("Inside function:",arg)
   print ("ID inside the function:", id(arg))
   arg=arg.append(100)
   
   
var=[10, 20, 30, 40]
print ("ID before passing:", id(var))
testfunction(var)
print ("list after function call", var)
print ("ID inside the function after modified the argument:", id(var))


def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))



# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )



def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   return val

phy = 60
maths = 70
result = percent(phy,maths)
print ("percentage:", result)

phy = 40
maths = 46
result = percent(phy,maths, 100)
print ("percentage:", result)


# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Naveen", 29)

# by keyword arguments
printinfo(name="miki", age = 30)



def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(5, den=10)