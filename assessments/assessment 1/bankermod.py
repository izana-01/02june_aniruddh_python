acc={}
import datetime
def account():
    account_number = input("Enter account number: ")
    account_name = input("Enter account holder name: ")
    account_balance = float(input("Enter opening balance: "))
    acc[account_number] = {
        "name": account_name,
        "balance": account_balance,
        "created at": str(datetime.datetime.now())}
    ao=open("account.txt", "a")
    ao.write(f"Account Number: {account_number}, Name: {account_name}, Balance: {account_balance}, Created at: {acc[account_number]['created at']}\n")
    ao.close()
    
def viewall_account():
        print("All accounts:")
        with open("account.txt", "r") as file:
            print(file.read())

def search_account():
    account_number = input("Enter account number to search: ")
    if account_number in acc:
        print(f"Account found: {acc[account_number]}")
    else:
        print("Account not found.")

def view_customer():
    print("Viewing all customers...")
    viewall_account()
    if not acc:
        print("No customers found.")
    else:
        for acc_num, details in acc.items():
            print(f"Account Number: {acc_num}, Details: {details}")


def total_amount_in_bank():
    total_balance = sum(details["balance"] for details in acc.values())
    print(f"Total amount in bank: {total_balance}")
