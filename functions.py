def greet():
    print("Hello welcome!")

greet()

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# Default parameter value
def greet(name="Guest"):
    print("Hello,", name)

greet("Bob")

# Function with multiple return values
def get_details():
    name = "Lalithya"
    age = 25
    return name, age

n, a = get_details()
print("Name:", n, "| Age:", a)

# Function with *args (Multiple Arguments)
def add_all(*numbers):
    return sum(numbers)  # sum is a predefined function

print(add_all(1, 2, 3, 4, 5))

# Function with **kwargs (Keyword Arguments)
def info(**details):
    for key, value in details.items():
        print(key, ":", value)  # ✅ Fixed print statement

info(name="Lalithya", age=25, city="Nellore")
