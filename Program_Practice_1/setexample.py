StopAsyncIterations1 = {"Rohan", "Physics", 21, 69.75}
s2 = {1, 2, 3, 4, 5}
s3 = {"a", "b", "c", "d"}
s4 = {25.50, True, -55, 1+2j}
print (s1)
print (s2)
print (s3)
print (s4)


L1 = ["Rohan", "Physics", 21, 69.75]
s1 = set(L1)
T1 = (1, 2, 3, 4, 5)
s2 = set(T1)
string = "TutorialsPoint"
s3 = set(string)

print (s1)
print (s2)
print (s3)

#Set is a collection of distinct objects. Even if you repeat an object in the collection, only one copy is retained in it.
s2 = {1, 2, 3, 4, 5, 3,0, 1, 9}
s3 = {"a", "b", "c", "d", "b", "e", "a"}
print (s2)
print (s3)


#You can only traverse the set items using a for loop for set
langs = {"C", "C++", "Java", "Python"}
for lang in langs:
   print (lang,"\n")


#Python's membership operators let you check if a certain item is available in the set. 
langs = {"C", "C++", "Java", "Python"}
print ("PHP" in langs)
print ("Java" in langs)

#The following example shows how the union() method works −
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = lang1.union(lang2)
print (lang3)

#The following example shows how the union() method works −
lang1 = {"C", "C++", "Java", "Python"}
print(lang1)
lang2 = {"PHP", "C#", "Perl"}
print(lang2)
lang3 = lang1.update(lang2)
print (lang1)
print(lang3 )

#If a sequence object is given as argument to union() method, Python automatically converts it to a set first and then performs union.
lang1 = {"C", "C++", "Java", "Python"}
lang2 = ["PHP", "C#", "Perl"]
lang3 = lang1.union(lang2)
print (lang3)

#In this example, a set is constructed from a string, and another string is used as argument for union() method.
set1 = set("Hello")
print(set1)
set2 = set1.union("World")
print (set2)
print(set("krishnendu"))

#The remove() method removes the given item from the set collection, if it is present in it. However, if it is not present, it raises KeyError.
lang1 = {"C", "C++", "Java", "Python"}
print ("Set before removing: ", lang1)
lang1.remove("Java")
print ("Set after removing: ", lang1)
#lang1.remove("PHP")

#The discard() method in set class is similar to remove() method. The only difference is, it doesn't raise error even if the object to be removed is not already present in the set collection.*/
lang1 = {"C", "C++", "Java", "Python"}
print ("Set before discarding C++: ", lang1)
lang1.discard("C++")
print ("Set after discarding C++: ", lang1)
print ("Set before discarding PHP: ", lang1)
lang1.discard("PHP")
print ("Set after discarding PHP: ", lang1)

#The pop() method returns the object removed from set.
lang1 = {"C", "C++"}
print ("Set before popping: ", lang1)
obj = lang1.pop()
print ("object popped: ", obj)
print ("Set after popping: ", lang1)
obj = lang1.pop()

#The clear() method in set class removes all the items in a set object, leaving an empty set.
lang1 = {"C", "C++", "Java", "Python"}
print (lang1)
print ("After clear() method")
lang1.clear()
print (lang1)

#The difference_update() method in set class updates the set by removing items that are common between itself and another set given as argument.
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)


capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana'))


d1=dict([('a', 100), ('b', 200), ('c', 'one'), ('d', 'two')]) # this is list
d2 = dict((('a', 'one'), ('b', 'two'))) # This is Tuple
print ('d1: ', d1)
print ('d2: ', d2)

d1=dict(a= 100, b=200, c=300)
d2 = dict(a='one', b='two', c="Three")
print ('d1: ', d1)
print ('d2: ', d2)

#The existing dictionary is updated with new key-value pairs added to it.
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks.update(marks1)
print ("marks dictionary after update: \n", marks)


#Two dictionaries are merged and a new object is returned.
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print (x)


import array as arr
a = arr.array('d', [1, 2, 3])
l = len(a)
idx =0
while idx<l:
   print (a[idx])
   idx+=1


import array as arr
a = arr.array('d', [1, 2, 3])
l = len(a)
for x in range(l):
   print (a[x])



import array, copy
a = arr.array('i', [1, 2, 3, 4, 5])
#import copy
b = copy.deepcopy(a)
print (id(a), id(b))
a[2]=10
print (a,b)
print (id(a), id(b))


import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print (a, b)

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
b = a.tolist()
print (b)
b.reverse()
print (b)
a = arr.array('i')
a.fromlist(b)
print (a)

import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print (a)


import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
for i in range(len(b)):
   a.append(b[i])
print (a, b)


import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x=a.tolist()
y=b.tolist()
z=x+y
a=arr.array('i')
a.fromlist(z)
print (a)


import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
a.extend(b)
print (a)

import array as arr
f = open('list.txt','wb')
arr.array("i", [10, 20, 30, 40, 50]).tofile(f)

f.close()
f = open("list.txt", "rb")
a.fromfile(f, 5)
print (a)
f.close()











