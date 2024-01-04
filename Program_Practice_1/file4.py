f=open('test.bin', 'wb')
data=b"Hello World"
f.write(data)
f.close()
f=open('test.bin', 'rb')
data1=f.read()
print (data1.decode(encoding='utf-8'))
f.close()