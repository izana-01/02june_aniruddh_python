#Write a Python program to read the contents of a file and print them on the console.
with open("example.txt", "r") as f:
    content = f.read()
    print(content)