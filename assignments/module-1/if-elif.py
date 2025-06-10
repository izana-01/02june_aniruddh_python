a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))

if a>b and a>c:
    print("A is max")
elif b>c and b>a:
    print("B is max")
else:
    print("C is max")