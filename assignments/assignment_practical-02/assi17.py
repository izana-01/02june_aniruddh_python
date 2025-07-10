#Write a Python program to access alternate values between index 1 and 5 in a tuple.
tuple = ("apple", "banana", "cherry", "orange", "grape", "mango", "kiwi")

altvalues = tuple[1:5:2]

print("Original tuple:")
print(tuple)

print("Alternate values from index 1 to 4:")
print(altvalues)
