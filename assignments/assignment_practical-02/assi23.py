#Write a Python program to convert two lists into one dictionary using a for loop. 
keys = ["name", "age", "course"]
values = ["izana", 20, "DS"]

dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]

print("Dictionary created from two lists:")
print(dict)