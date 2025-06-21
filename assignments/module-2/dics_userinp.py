"""data = {}

n = int(input("Enter a number of pair:"))



for i in range(n):
    x = input("Enter your key's:")
    y = input("Enter your value:")
    data[x]=y

print(data)  """

data = {}

keys=['id','name','city']


for i in range(len(keys)):
    x = input(f"Enter value of {keys[i]}:")
    data[keys[i]]=x

print(data)  