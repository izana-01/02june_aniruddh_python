n1 = int(input("num.1"))
n2 = int(input("num.2"))
 
print("1:add")
print("1:add")
print("1:add") 
print("1:add")

choice= int(input("enter ur choice:"))

if choice == 1:
    print("add.", n1+n2)

elif choice ==2:
    print("sub:", n1-n2)

elif choice ==3:
    print("mul:", n1*n2)

elif choice ==4:
    print("div:", n1/n2)

else:
    print ("error:invalid choice....")
