#Write a Python program to import the math module and use functions like sqrt(), ceil(), floor(). 

import math

a = float(input("Enter a number: "))

squareroot = math.sqrt(a)
ceilvalue = math.ceil(a)
floorvalue = math.floor(a)

print("Results using math module:")
print("Square root:", squareroot)
print("Ceiling value:", ceilvalue)
print("Floor value:", floorvalue)