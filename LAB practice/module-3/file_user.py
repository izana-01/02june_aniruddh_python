y=open("new.txt","a")
"""y=open("new.txt","w")"""

"""y.write(input("id:"))
y.write(input("name:"))
y.write(input("city:"))"""

"""id=input("id:")
name=input("name:")
city=input("city:")

y.write(f"ID:{id}\nNAME:{name}\nCITY:{city}")"""

c=int(input("how many data:"))

for i in range(c):

   id=input("id:")
   name=input("name:")
   city=input("city:")

   y.write(f"ID:{id}\nNAME:{name}\nCITY:{city}\n")