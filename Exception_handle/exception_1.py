#!/usr/bin/python

def main():
    try:
        fh=open("krishnendu.txt","w")
        fh.write("This is a file exception program")
        x = 1 / 0
        fh.read()
    except ZeroDivisionError as e:
        print("Can not divided by zero", e)
    except IOError as e:
        print("This is io error ", e)
    finally:
        print("All are good!")
        fh.close()

main()