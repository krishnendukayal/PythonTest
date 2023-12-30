s1="WORD"
print ("original string:", s1)
l1=list(s1)

l1.insert(3,"L")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)

str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1+str2*3
print("String 3:",str3)
str4=(str1+str2)*3
print ("String 4:", str4)

var = "This Is String Example....WOW!!!"
var1 = var.center(60, '*')
print ("original string:", var)
print ("Centered string:", var1)


var = "This Is String Example....WOW!!!"
var1 = var.ljust(40, '*')

print ("original string:", var)
print ("Left justified string:", var1)


var = "This Is String Example....WOW!!!"
var1 = var.rjust(40, '*')

print ("original string:", var)
print ("Left justified string:", var1)


lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])

test=[]
for i in "krishnendu":
   if i not in "aeiou":
      test.append(i)
print(test)   

squares = [x*x for x in range(1,11)]
print (squares)

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L3 = L1+L2
print ("Joined list:", L3)

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1+=L2
print ("Joined list:", L1)


L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1.extend(L2)
print ("Joined list:", L1)

L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']

for x in L2:
   L1.append(x)
   
print ("Joined list:", L1)



a=[1,1,1,2,23,5,56,6,7,7,7]
b=[]
for i in a:
   if i not in b:
      b.append(i)
print(b)      


T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)

T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Joined Tuple:", T3)