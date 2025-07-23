# Write a Python program to write multiple strings into a file.
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example2.txt", "w") as f:
    f.writelines(lines)