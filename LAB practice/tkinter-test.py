import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import os
import subprocess
import sys


def new_file():
    messagebox.showinfo("New File", "New file created!")

def open_file():
    messagebox.showinfo("Open File", "File opened!")

def save_file():
    messagebox.showinfo("Save File", "File saved!")

def exit_app():
    root.quit()

def open_calculator():
    try:
        if sys.platform == "win32":
            subprocess.Popen("calc")
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-a", "Calculator"])
        else:
            subprocess.Popen(["gnome-calculator"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open calculator:\n{e}")

def open_notepad():
    try:
        if sys.platform == "win32":
            subprocess.Popen("notepad")
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-a", "TextEdit"])
        else:
            subprocess.Popen(["gedit"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open notepad:\n{e}")

def open_chrome():
    try:
        if sys.platform == "win32":
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-a", "Google Chrome"])
        else:
            subprocess.Popen(["google-chrome"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open Chrome:\n{e}")

def show_about():
    messagebox.showinfo("About", "Name: Aniruddh Dabhi\nRole: Developer\nVersion: 1.0")

def show_contact():
    messagebox.showinfo("Contact", "Phone: 9825917373")

# Create main window
root = tk.Tk()
root.title("my app")
root.geometry("400x300")
root.geometry("400x600")
root.config(bg="gray")

try:
    root.iconbitmap(r"C:\Users\Anirudh\OneDrive\Pictures\zoro.webp")  # Replace with your actual path
except Exception as e:
    print("Could not set icon:", e)


# Create menu bar
menubar = tk.Menu(root)

# Fine Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Apps Menu
apps_menu = tk.Menu(menubar, tearoff=0)
apps_menu.add_command(label="Calculator", command=open_calculator)
apps_menu.add_command(label="Notepad", command=open_notepad)
apps_menu.add_command(label="Google Chrome", command=open_chrome)
menubar.add_cascade(label="Apps", menu=apps_menu)

# About Menu
about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="About Me", command=show_about)
menubar.add_cascade(label="About", menu=about_menu)

# Contact Menu
contact_menu = tk.Menu(menubar, tearoff=0)
contact_menu.add_command(label="Contact Info", command=show_contact)
menubar.add_cascade(label="Contact", menu=contact_menu)

# Configure the window to use the menubar
root.config(menu=menubar)

root.mainloop()
