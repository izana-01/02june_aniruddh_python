#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input)
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")

try:
    x = int(input("Enter number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)