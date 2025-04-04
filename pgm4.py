class Dog:
    
    species = "Canine"
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age

#create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)
#Access class, instance
print(dog1.species) #c.v
print(dog1.name) #i.v
print(dog2.name) #i.v

#Modify instance
dog1.name = "Max"
print(dog1.name)