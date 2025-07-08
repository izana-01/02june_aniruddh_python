# Write a Python program to create a calculator using functions. 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Simple Calculator")
print("Choose operation: ")

operation = input("Enter operation: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation!"

print("Result:", result)