import tkinter as tk
import sqlite3

try:
    con=sqlite3.connect("ecommerce.db")
    print("Database connected successfully")
except Exception as e:
    print(e)
crt='create table product(pid integer, pname text, qty integer, price real)'
try:
    con.execute(crt)
    con.commit()
except Exception as e:
    print(e)

#main GUI
window= tk.Tk()
window.title("E-Commerce APP")
window.geometry("500x250")
window.config(bg="grey")

tk.Label(text="PID", bg="grey", fg="white", font=("Arial", 18, "bold")).grid(row=0, column=0,sticky="n",columnspan=2)
tk.Label(text="PNAME", bg="grey", fg="white", font=("Arial", 18, "bold")).grid(row=0, column=2,sticky="w",columnspan=2)
tk.Label(text="QTY", bg="grey", fg="white", font=("Arial", 18, "bold")).grid(row=0, column=3,sticky="w",columnspan=2)
tk.Label(text="PRICE", bg="grey", fg="white", font=("Arial", 18, "bold")).grid(row=0, column=4,sticky="w",columnspan=2)

id=tk.Entry( )
id.grid(row=1, column=0)
name=tk.Entry( )
name.grid(row=1, column=2)
qty=tk.Entry( )
qty.grid(row=1, column=3)
price=tk.Entry( )
price.grid(row=1, column=4)

def submit():
    pid = int(id.get())
    pname = str(name.get())
    qauntity = int(qty.get())
    prc = float(price.get())
    
    try:
        con.execute("INSERT INTO product (pname, qty, price) VALUES (?, ?, ?)", (pname, qauntity, prc))
        con.commit()
        print("Product added successfully")
    except Exception as e:
        print(e)

submit_entry= tk.Button(text="Submit", bg="green", fg="white",command=submit, font=("Arial", 18, "bold"))
submit_entry.grid(row=5, column=2, sticky="w")

window.mainloop()

