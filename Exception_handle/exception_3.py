try:
    f=open("krishnendu1.txt")

except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
else:
    ff = f.read()
    print(ff)
    f.close()
finally:
    print("Finally !!")