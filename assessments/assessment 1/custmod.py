acc={}
a="a"
b="a"
c="a"
d=0

import datetime

def deposite():
    global d
    depo=int(input("Enter the amount to deposit: "))
    d += depo
    print(f"Deposited: {depo},deposited at: {str(datetime.datetime.now())}")

def withdraw():
    global d
    if d <= 0:
        print("Insufficient balance to withdraw.")
        return
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    if withdraw_amount > d:
        print("Withdrawal amount exceeds current balance.")
    else:
        d -= withdraw_amount
        print(f"Withdrawn: {withdraw_amount},withdraw at: {str(datetime.datetime.now())}")

def view_balance():
    global d
    print(f"Current balance: {d}")