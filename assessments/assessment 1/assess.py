import bankermod as bd

import custmod as cd


def bank_manager():
    while True:
        print("Welcome To Bank Manager System")
        print("\n \t operation menu")
        print("\n \t 1) add customer")
        print("\n \t 2) view customer")
        print("\n \t 3) search customer")
        print("\n \t 4) view customer")
        print("\n \t 5) total amount in bank")

        choice= int(input("\n \t Enter your choice: "))
        if choice == 1:
            bd.account()
        elif choice == 2:
            bd.viewall_account()
        elif choice == 3:
            bd.search_account()
        elif choice == 4:
            bd.view_customer()
        elif choice == 5:
            bd.total_amount_in_bank()
        else:
            print("Invalid choice, please try again.")
        break



def customer_operations():
    while True:
        print("Welcome to Customer Operations")
        print("\n \t operation menu")
        print("\n \t 1) deposit")
        print("\n \t 2) withdraw")
        print("\n \t 3) view balance")

        choice = int(input("\n \t Enter your choice: "))
        if choice == 1:
            cd.deposite()
        elif choice == 2:
            cd.withdraw()
        elif choice == 3:
            cd.view_balance()
        else:
            print("Invalid choice, please try again.")
        break 


