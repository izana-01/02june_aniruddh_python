import assess as ad
import bankermod as bd
import custmod as cd

def maincode():
    while True:
        print(" \t WELCOME TO PYTHON BANK MANAGEMENT SYSTEM ")
        print(" select your role:\n 1. Bank Manager \n 2. Customer \n 3.Exit \n")
        role= input("Enter '1' for Bank Manager or '2' for Customer: ")
        if role=='1':
            ad.bank_manager()
        elif role=='2':        
            ad.customer_operations()
        elif role=='3':
            break
        else:
            print("Invalid role selected. Please try again.")


maincode()

