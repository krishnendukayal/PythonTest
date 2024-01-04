#Read Float Data from File
import struct
x=233.50
data=struct.pack('f',x)
f=open('test2.bin', 'wb')
f.write(data)
f=open('test2.bin', 'rb')
data=f.read()
x=struct.unpack('f', data)
print (x)   