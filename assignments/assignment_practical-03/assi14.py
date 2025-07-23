# Write a Python program to create a class and access the properties of the class using an object. 
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Aniruddh")
print("Name:", p.name)