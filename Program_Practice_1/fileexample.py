# Open a file
import os
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opened file
fo.close()

fo=open("foo.txt","w+")
fo.write("This is a rat race")
text = fo.read(5)
print (text)
fo.seek(10,0)
data=fo.read(3)
fo.seek(10,0)
fo.write('cat')
text = fo.read()
print (text)

fo.close()
