import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re

# ========== DATABASE SETUP ==========
conn = sqlite3.connect("repairmate.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    model TEXT,
    issue TEXT,
    status TEXT,
    technician TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    device_id INTEGER,
    cost REAL,
    tax REAL,
    total REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(device_id) REFERENCES devices(id)
)
""")
conn.commit()


# ========== CLASSES ==========
class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (self.name, self.phone))
        conn.commit()
        return cursor.lastrowid


class Device:
    def __init__(self, customer_id, model, issue, status="Pending", technician=""):
        self.customer_id = customer_id
        self.model = model
        self.issue = issue
        self.status = status
        self.technician = technician

    def save(self):
        cursor.execute("""INSERT INTO devices (customer_id, model, issue, status, technician) 
                          VALUES (?, ?, ?, ?, ?)""",
                       (self.customer_id, self.model, self.issue, self.status, self.technician))
        conn.commit()
        return cursor.lastrowid


class Invoice:
    def __init__(self, customer_id, device_id, cost, tax_percent):
        self.customer_id = customer_id
        self.device_id = device_id
        self.cost = cost
        self.tax_percent = tax_percent
        self.total = self.calculate_total()

    def calculate_total(self):
        try:
            return self.cost + (self.cost * self.tax_percent / 100)
        except ZeroDivisionError:
            return self.cost

    def save(self):
        cursor.execute("""INSERT INTO invoices (customer_id, device_id, cost, tax, total)
                          VALUES (?, ?, ?, ?, ?)""",
                       (self.customer_id, self.device_id, self.cost, self.tax_percent, self.total))
        conn.commit()


# ========== GUI ==========
class RepairMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RepairMate - TechRepair Hub")
        self.root.geometry("900x600")

        self.tab_control = ttk.Notebook(root)
        self.customer_tab = ttk.Frame(self.tab_control)
        self.device_tab = ttk.Frame(self.tab_control)
        self.invoice_tab = ttk.Frame(self.tab_control)
        self.search_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.customer_tab, text="Customer")
        self.tab_control.add(self.device_tab, text="Device")
        self.tab_control.add(self.invoice_tab, text="Invoice")
        self.tab_control.add(self.search_tab, text="Search")
        self.tab_control.pack(expand=1, fill="both")

        self.setup_customer_tab()
        self.setup_device_tab()
        self.setup_invoice_tab()
        self.setup_search_tab()

    # ===== CUSTOMER TAB =====
    def setup_customer_tab(self):
        tk.Label(self.customer_tab, text="Customer Name").grid(row=0, column=0)
        tk.Label(self.customer_tab, text="Phone").grid(row=1, column=0)

        self.cust_name = tk.Entry(self.customer_tab)
        self.cust_phone = tk.Entry(self.customer_tab)

        self.cust_name.grid(row=0, column=1)
        self.cust_phone.grid(row=1, column=1)

        tk.Button(self.customer_tab, text="Add Customer", command=self.add_customer).grid(row=2, column=0, columnspan=2)

        self.customer_list = tk.Listbox(self.customer_tab, width=50)
        self.customer_list.grid(row=3, column=0, columnspan=2)
        self.load_customers()

    def add_customer(self):
        name = self.cust_name.get()
        phone = self.cust_phone.get()
        if not name or not phone:
            messagebox.showerror("Error", "All fields are required")
            return
        customer = Customer(name, phone)
        customer.save()
        messagebox.showinfo("Success", "Customer added")
        self.cust_name.delete(0, tk.END)
        self.cust_phone.delete(0, tk.END)
        self.load_customers()

    def load_customers(self):
        self.customer_list.delete(0, tk.END)
        cursor.execute("SELECT id, name, phone FROM customers")
        for c in cursor.fetchall():
            self.customer_list.insert(tk.END, f"{c[0]} - {c[1]} ({c[2]})")

    # ===== DEVICE TAB =====
    def setup_device_tab(self):
        tk.Label(self.device_tab, text="Customer ID").grid(row=0, column=0)
        tk.Label(self.device_tab, text="Device Model").grid(row=1, column=0)
        tk.Label(self.device_tab, text="Issue").grid(row=2, column=0)
        tk.Label(self.device_tab, text="Technician").grid(row=3, column=0)

        self.device_cust_id = tk.Entry(self.device_tab)
        self.device_model = tk.Entry(self.device_tab)
        self.device_issue = tk.Entry(self.device_tab)
        self.device_tech = tk.Entry(self.device_tab)

        self.device_cust_id.grid(row=0, column=1)
        self.device_model.grid(row=1, column=1)
        self.device_issue.grid(row=2, column=1)
        self.device_tech.grid(row=3, column=1)

        tk.Button(self.device_tab, text="Add Device", command=self.add_device).grid(row=4, column=0, columnspan=2)

        self.device_list = tk.Listbox(self.device_tab, width=60)
        self.device_list.grid(row=5, column=0, columnspan=2)
        self.load_devices()

    def add_device(self):
        try:
            customer_id = int(self.device_cust_id.get())
        except ValueError:
            messagebox.showerror("Error", "Customer ID must be a number")
            return
        model = self.device_model.get()
        issue = self.device_issue.get()
        tech = self.device_tech.get()
        if not model or not issue:
            messagebox.showerror("Error", "Model and Issue required")
            return
        device = Device(customer_id, model, issue, technician=tech)
        device.save()
        messagebox.showinfo("Success", "Device added")
        self.device_cust_id.delete(0, tk.END)
        self.device_model.delete(0, tk.END)
        self.device_issue.delete(0, tk.END)
        self.device_tech.delete(0, tk.END)
        self.load_devices()

    def load_devices(self):
        self.device_list.delete(0, tk.END)
        cursor.execute("SELECT id, customer_id, model, status, technician FROM devices")
        for d in cursor.fetchall():
            self.device_list.insert(tk.END, f"{d[0]} - Cust:{d[1]} | {d[2]} | {d[3]} | Tech:{d[4]}")

    # ===== INVOICE TAB =====
    def setup_invoice_tab(self):
        tk.Label(self.invoice_tab, text="Customer ID").grid(row=0, column=0)
        tk.Label(self.invoice_tab, text="Device ID").grid(row=1, column=0)
        tk.Label(self.invoice_tab, text="Cost").grid(row=2, column=0)
        tk.Label(self.invoice_tab, text="Tax %").grid(row=3, column=0)

        self.invoice_cust_id = tk.Entry(self.invoice_tab)
        self.invoice_device_id = tk.Entry(self.invoice_tab)
        self.invoice_cost = tk.Entry(self.invoice_tab)
        self.invoice_tax = tk.Entry(self.invoice_tab)

        self.invoice_cust_id.grid(row=0, column=1)
        self.invoice_device_id.grid(row=1, column=1)
        self.invoice_cost.grid(row=2, column=1)
        self.invoice_tax.grid(row=3, column=1)

        tk.Button(self.invoice_tab, text="Generate Invoice", command=self.add_invoice).grid(row=4, column=0, columnspan=2)

        self.invoice_list = tk.Listbox(self.invoice_tab, width=60)
        self.invoice_list.grid(row=5, column=0, columnspan=2)
        self.load_invoices()

    def add_invoice(self):
        try:
            cust_id = int(self.invoice_cust_id.get())
            dev_id = int(self.invoice_device_id.get())
            cost = float(self.invoice_cost.get())
            tax = float(self.invoice_tax.get())
        except ValueError:
            messagebox.showerror("Error", "All fields must be valid numbers")
            return
        invoice = Invoice(cust_id, dev_id, cost, tax)
        invoice.save()
        messagebox.showinfo("Success", f"Invoice Total: {invoice.total}")
        self.invoice_cust_id.delete(0, tk.END)
        self.invoice_device_id.delete(0, tk.END)
        self.invoice_cost.delete(0, tk.END)
        self.invoice_tax.delete(0, tk.END)
        self.load_invoices()

    def load_invoices(self):
        self.invoice_list.delete(0, tk.END)
        cursor.execute("SELECT id, customer_id, device_id, total FROM invoices")
        for inv in cursor.fetchall():
            self.invoice_list.insert(tk.END, f"{inv[0]} - Cust:{inv[1]} | Dev:{inv[2]} | Total:{inv[3]}")

    # ===== SEARCH TAB =====
    def setup_search_tab(self):
        tk.Label(self.search_tab, text="Search Pattern").grid(row=0, column=0)
        self.search_entry = tk.Entry(self.search_tab)
        self.search_entry.grid(row=0, column=1)
        tk.Button(self.search_tab, text="Search Devices", command=self.search_devices).grid(row=0, column=2)

        self.search_results = tk.Listbox(self.search_tab, width=80)
        self.search_results.grid(row=1, column=0, columnspan=3)

    def search_devices(self):
        pattern = self.search_entry.get()
        self.search_results.delete(0, tk.END)
        cursor.execute("SELECT id, model, status FROM devices")
        for d in cursor.fetchall():
            if re.search(pattern, f"{d[1]} {d[2]}", re.IGNORECASE):
                self.search_results.insert(tk.END, f"{d[0]} | {d[1]} | {d[2]}")


# ========== RUN APP ==========
root = tk.Tk()
app = RepairMateApp(root)
root.mainloop()
    