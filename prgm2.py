class Dog:
    species = "Canine"
    
    def __init__(self, name, age):
        self.name = name #Instance attribute
        self.age = age #instance attribute
#creating an object of dog class
dog1=Dog()
dog1=Dog("Buddy", 3)

print(dog1.name)#buddy
print(dog1.species)#canine