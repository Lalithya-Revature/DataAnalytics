import os
try:
    with open("text.txt", "r") as file:
        data = file.read()

    with open("text1.txt", "w") as filewrite:
        filewrite.write(data)

    print("File copied successfully")

except FileNotFoundError:
    print("Input or output file not found")

except OSError as e:
    print(f"I/O Exception: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
