#Write a Python program to remove elements from a list using pop() and remove().
fruits = ["apple", "banana", "cherry", "orange", "lemon"]

print("Original list:")
print(fruits)

print("\nUsing remove to delete:")
fruits.remove("banana")  
print("after remove:", fruits)

print("\nUsing pop to remove the element at index 2:")
removed_item = fruits.pop(2)  
print("Removed item:", removed_item)
print("List after pop:", fruits)
