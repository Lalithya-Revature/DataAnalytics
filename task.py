#grades
marks=int(input("enter marks :"))
if marks>=90 and marks<=100:
    print("grade A")
elif marks>=80 and marks<90:
    print("grade B")
elif marks>=70 and marks<80:
    print("grade C")
elif marks>=60 and marks<70:
    print("grade D")
else:
    print("fail")

# palindrome
a="lalithya"
k=a[::-1]
if k==a:
    print("palindrome")
else:
    print("not palindrome")
##############################
n=int(input("enter number :"))
orig=n
rev=0
while n!=0:
    temp=n%10
    rev=rev*10+temp
    n=n//10
if rev==orig:
    print("palindrome")
else:
    print("not palindrome")
 
   
# prime
n=int(input("enter value :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not prime")
    
# even or not
n=int(input("enter number:"))
if n%2==0:
    print("Even number")
else:
    print("odd number")

# -------------------- Single Inheritance --------------------
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def welcome(self):
        print("Hello from Child")

print("\n--- Single Inheritance ---")
obj = Child()
obj.greet()
obj.welcome()

# -------------------- Multilevel Inheritance --------------------
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def say_hello(self):
        print("Hello from Parent")

class Child(Parent):
    def bye(self):
        print("Bye from Child")

print("\n--- Multilevel Inheritance ---")
obj = Child()
obj.greet()
obj.say_hello()
obj.bye()

# -------------------- Hierarchical Inheritance --------------------
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def hello(self):
        print("Welcome from Child 1")

class Child2(Parent):
    def bye(self):
        print("Bye from Child 2")

print("\n--- Hierarchical Inheritance ---")
obj1 = Child1()
obj2 = Child2()
obj1.greet()
obj1.hello()
obj2.greet()
obj2.bye()

# -------------------- Multiple Inheritance --------------------
class A:
    def hello(self):
        print("Hello to multiple inheritance")

class B:
    def welcome(self):
        print("Welcome all")

class C(A, B):
    pass

print("\n--- Multiple Inheritance ---")
obj = C()
obj.hello()
obj.welcome()

# -------------------- Hybrid Inheritance --------------------
class A:
    def methodA(self):
        print("Method A")

class B(A):
    def methodB(self):
        print("Method B")

class C(A):
    def methodC(self):
        print("Method C")

class D(B, C):
    def methodD(self):
        print("Method D")

print("\n--- Hybrid Inheritance ---")
obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()

# -------------------- Method Overloading (Simulated) --------------------
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

print("\n--- Method Overloading ---")
calc = Calculator()
print(calc.add(5))          # 5
print(calc.add(5, 3))       # 8
print(calc.add(5, 3, 2))    # 10

# -------------------- Method Overriding --------------------
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

print("\n--- Method Overriding ---")
a = Animal()
d = Dog()
print(a.sound())  # Some sound
print(d.sound())  # Bark

# -------------------- Public Variable --------------------
class Car:
    def __init__(self):
        self.brand = "Toyota"

print("\n--- Public Variable ---")
c = Car()
print(c.brand)

# -------------------- Protected Variable --------------------
class Car:
    def __init__(self):
        self._speed = 120

class SportsCar(Car):
    def show_speed(self):
        print("Speed:", self._speed)

print("\n--- Protected Variable ---")
s = SportsCar()
s.show_speed()
print(s._speed)

# -------------------- Private Variable --------------------
class Car:
    def __init__(self):
        self.__engine_number = "ABC123"

    def show_engine(self):
        print(self.__engine_number)

print("\n--- Private Variable ---")
c = Car()
c.show_engine()
# Accessing private via name mangling
print(c._Car__engine_number)
