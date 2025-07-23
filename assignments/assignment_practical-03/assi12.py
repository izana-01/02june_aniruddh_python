#Write a Python program to handle file exceptions and use the finally block for closing the file 
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleaning up...")