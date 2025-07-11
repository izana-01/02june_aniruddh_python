#Write a Python program to create a lambda function with one expression. 

square = lambda x: x * x

a = int(input("Enter a number: "))
result = square(a)

print("Square of", a, "is:", result)