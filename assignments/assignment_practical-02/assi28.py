#Write a Python program to create a lambda function with two expressions. 
add = lambda x, y: x + y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add(a, b)

print("Sum:", result)