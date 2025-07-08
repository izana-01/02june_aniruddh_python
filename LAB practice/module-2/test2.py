import datetime

def billing_system():
    total=0
    items=[]

    while True:
        name=input("Enter your name: ")
        mobile=input("Enter your mobile number: ")
        food=input("Enter food name:")
        qty=int(input("How many items do  u want:"))
        price=float(input("What is the price of your item:"))
        

        item_total= qty * price
        total += item_total
        gst = item_total * 0.18
        
        items.append((name,mobile,food,qty,price, item_total,gst))

        more= input(" Do you want moe items? (1 for yes/2 for no):")
        if more == '1':
            continue
        elif more == '2':
            print("Thank you for your order!")
            break
        

    print("\n ----------------   Bill Summary ------------------- \n ")
    
 

    print("\n GRAND TOTAL : ", (total * 0.18) + total) 

    
    x=open("food_bill.txt", "a")
    x.write('Created at:'+str(datetime.datetime.now()))
    x.write("\n -----------------   Bill Summary ------------------ \n ")
    
    x.write("\n GRAND TOTAL : " + str((total * 0.18) + total))



billing_system()