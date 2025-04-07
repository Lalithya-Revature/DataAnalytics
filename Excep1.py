class UserNotFound(Exception):
    pass
try:
    username = input("Enter your username: ")
    if username != "Remya":
        raise UserNotFound("User not found. Please check the username.")
    print("Welcome,", username)
except UserNotFound as e:
    print(e)
finally:
    print("Code executed successfully.")
