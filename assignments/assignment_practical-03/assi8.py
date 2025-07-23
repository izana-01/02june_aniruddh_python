#4 & 5: Create, write, and read file
with open("sample.txt", "w") as f:
    f.write("Python is fun!")

with open("sample.txt", "r") as f:
    print(f.read())
