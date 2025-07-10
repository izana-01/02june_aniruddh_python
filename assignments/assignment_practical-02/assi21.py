#Write a Python program to merge two lists into one dictionary using a loop. 
keys = ["name", "age", "course"]
values = ["izana", 20, "DS"]

mdict = {}

for i in range(len(keys)):
    mdict[keys[i]] = values[i]

print("Merged Dictionary:")
print(mdict)