#Local scope
def myfunc():
    x = 600
    print(x)
myfunc()

#Enclosing
def myfunc():
    x = 400
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

#Global scope
x = 200
def myfunc():
    print(x)
myfunc()
print(x)