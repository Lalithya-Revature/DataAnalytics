class Parent():
    def show(self):
        print("Inside Parent")
        
class Child(Parent):
    def show(self):
        super().show()
        print("Inside child")
        
obj = Child()
obj.show()