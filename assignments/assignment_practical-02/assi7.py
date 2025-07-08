#Write a Python program to sort a list using both sort() and sorted().
numbers = [5, 2, 9, 1, 7]

print("Original list:")
print(numbers)

sorted = sorted(numbers)
print("\nList sorted using sorted:")
print(sorted)

numbers.sort()
print("\nList after using sort:")
print(numbers)