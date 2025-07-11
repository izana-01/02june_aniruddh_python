#Write a Python program to add elements to a list using insert() and append().
my_list = []

print("Adding elements append():")
my_list.append("apple")
my_list.append("pineapple")
my_list.append("cherry")

print("List after append():", my_list)

print("\nAdding elements insert():")
my_list.insert(1, "orange")  
my_list.insert(0, "pomogranate")   

print("List after insert():", my_list)