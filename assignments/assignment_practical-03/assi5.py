#Write a Python program to open a file in write mode, write some text, and then close it. 
file = open("example.txt", "w")
file.write("This is a sample string written to the file.")
file.close()