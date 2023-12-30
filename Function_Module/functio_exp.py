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

#Positional argument cannot appear after keyword arguments but viseversa is possible

def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(5, den=10)


def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg=arg+1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)
print ("ID after function call:", id(var))



def add(a, b):
   c=a+b
   return c

x=10
y=20
sum_add = add(x,y)
print("Addition of a = {} & b = {} are {}".format(x, y, sum_add))


def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(num=5, den=10)

def lala(*,a,b):
   c=a+b
   return c

zz=lala(a=12,b=23)
print(zz)


def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")




def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)



def lalu(**kwargs):
   for k,v in kwargs.items():
      print("{} : {}".format(k,v))
   return

lalu(math=80, sci=75, Eng=70, Hist=65, Geo=72)   

marks = 50 # this is a global variable
def myfunction():
   global marks
   marks = marks + 20
   print (marks)

myfunction()
print (marks) # prints global value

var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction():
   "Change values of global variables"
   globals()['var1'] = globals()['var1']+10
   global var2
   var2 = var2 + 20

myfunction()
print ("var1:",var1, "var2:",var2) #shows global variables with changed values


var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction(x, y):
   total = x+y
   print ("Total is a local variable: ", total)

myfunction(var1, var2)
#print (total) # This gives NameError

def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction.__annotations__)