try:
    x=10/0
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("Completed execution")