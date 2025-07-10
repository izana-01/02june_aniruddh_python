class BankSystem:
    def __init__(self):
        print("Welcome to the Bank Management System ")
        self.name = input("Enter Account Holder Name: ")
        self.acc_no = input("Enter Account Number: ")
        self.balance = 0
        self.run()

class viewall_account(BankSystem):
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.view_accounts()

    def view_accounts(self):
        print(f"Account Holder: {self.bank_system.name}")
        print(f"Account Number: {self.bank_system.acc_no}")
        print(f"Current Balance: {self.bank_system.balance}")

class Deposit(viewall_account):
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.deposit_amount()

    def deposit_amount(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.bank_system.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.bank_system.balance}")
        else:
            print("Invalid deposit amount.") 

class Withdraw(Deposit):
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.withdraw_amount()

    def withdraw_amount(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.bank_system.balance:
            self.bank_system.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.bank_system.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

class BankManagementSystem(Withdraw):
    def __init__(self):
        self.bank_system = BankSystem()
        self.run()

    def run(self):
        while True:
            print("\n1. View Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                viewall_account(self.bank_system)
            elif choice == '2':
                Deposit(self.bank_system)
            elif choice == '3':
                Withdraw(self.bank_system)
            elif choice == '4':
                print("Exiting the system. Thank you!")
                break
            else:
                print("Invalid choice, please try again.")

bk= BankManagementSystem()
bk.run()