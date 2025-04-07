import json

# JSON to Python
X = '{"name":"lalithya","age":22}'
z = json.loads(X)
print(z["name"])
print(z["age"])

# Dictionary to JSON format
X = {"name": "lavanya", "age": 26}
Y = json.dumps(X)
print(Y)
