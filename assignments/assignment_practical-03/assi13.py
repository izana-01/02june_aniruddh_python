#Write a Python program to print custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception!")
except CustomError as cus:
    print("Caught:", cus)