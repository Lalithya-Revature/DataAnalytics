import inspect
def decorator(func):
    
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

#Applying the decorator to a function
               
@decorator  #greet = decorator(greet)

def greet():
    print("Hello, World!")
greet()

print(inspect.signature(decorator))