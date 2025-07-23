#Write Python programs to demonstrate method overloading and method overriding 
class Overload:
    def greet(self, name=None):
        if name:
            print(f"Hello, {name}")
        else:
            print("Hello")

o = Overload()
o.greet()
o.greet("Aniruddh")




class Parent:
    def message(self):
        print("This is parent")

class Child(Parent):
    def message(self):
        print("This is child")

c = Child()
c.message()