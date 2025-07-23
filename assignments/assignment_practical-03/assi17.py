#Write a Python program to show multilevel inheritance. 
class A:
    def greet(self):
        print("Hello from A")

class C(A):
    def message(self):
        print("Message from C")

class D(C):
    pass

d = D()
d.greet()
d.message()
