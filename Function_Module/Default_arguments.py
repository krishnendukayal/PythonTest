#!/usr/bin/python

def defarg(name, age=33):
    print("%s is %d years old" %(name, age))
    return

defarg(name="krishnendu")

# IF YOU MENTION DEFAULT ASSIGNED VALUE FAST AND THEN NORMAL VALUE LIKE (AGE=30, NAME) THEN WILL GET ERROR
#    def defarg(age=33, name):
#SyntaxError: non-default argument follows default argument