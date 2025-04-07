try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError as e:
    print(f"Invalid Input: {e}")
except ZeroDivisionError as e:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Code executed successfully")
