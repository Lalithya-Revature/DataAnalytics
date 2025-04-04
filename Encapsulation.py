class Public:
    def __init__(self):
        self.__salary = 50000 # Private att double underscore
            
    def salary(self):
        return self.__salary #Access through public method
    
obj = Public()
print(obj.salary()) # works
# print(obj.__salary) # Raise AttributeError