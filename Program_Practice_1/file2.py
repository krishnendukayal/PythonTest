# Open a file in read-write mode
fo=open("foo.txt","w+")
fo.write("This is a rat race")
fo.seek(10,0)
data=fo.read(3)
print(data)
fo.seek(10,0)
fo.write('cat race and i don\'t lke this race')
fo.seek(0)
loco=fo.read()
print(loco)
fo.close()