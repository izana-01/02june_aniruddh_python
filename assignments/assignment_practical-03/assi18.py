#Write a Python program to show multiple inheritance. 
class X:
    def x_method(self):
        print("From X")

class Y:
    def y_method(self):
        print("From Y")

class Z(X, Y):
    pass

z = Z()
z.x_method()
z.y_method()
