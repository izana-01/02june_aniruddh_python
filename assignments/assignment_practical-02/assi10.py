#Write a Python program to create a tuple with multiple data types.
my_tuple = (25, "apple", 3.14, True, "banana")

print("Tuple with multiple data types:")
print(my_tuple)

print("\nEach element and its data type:")
for i in my_tuple:
    print(f"Value: {i}, Type: {type(i)}")