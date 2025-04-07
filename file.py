
file = open("test.txt", "r")

content = file.read()
print("Full Content:")
print(content)

# Reset the file pointer to the beginning
file.seek(0)

content1 = file.readline()
print("\nFirst Line:")
print(content1)
file.seek(0)
content2 = file.readlines()
print("\nAll Lines as List:")
print(content2)
file.close()
