#Write a Python program to count how many times each character appears in a string. 
text = input("Enter a value: ")

c = {}

for char in text:
    if char in c:
        c[char] += 1 
    else:
        c[char] = 1  

print("Characters :")
for key, value in c.items():
    print(f"'{key}' appears {value} time(s)")
