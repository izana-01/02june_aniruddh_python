#Write a Python program to demonstrate the use of local and global variables in a class. 
x = "global"

class Test:
    def show(self):
        x = "local"
        print("Local:", x)

print("Global:", x)
t = Test()
t.show()