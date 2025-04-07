class UserNotFoundException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise UserNotFoundException("Age must be 18 or above")
    else:
        print("You are eligible")
try:
    check_age(16)
except UserNotFoundException as e:
    print("Error:", e)
