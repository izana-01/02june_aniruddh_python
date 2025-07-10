#Write a python program to create a tuple with multiple data types.
tuple = (11, "abhi", 72.5, True)

print("Tuple with multiple data types:")
print(tuple)

print("\nEach element and its data type:")
for i in tuple:
    print("Value:", i, "| Type:", type(i))