import tkinter as tk
from tkinter import ttk, messagebox

def register():
    
    if not name_var.get().strip() or not contact_var.get().strip() or not email_var.get().strip():
        error_label.config(text="fill the empty field!!!")
    elif gender_var.get() not in ["Male", "Female"]:
        error_label.config(text="fill the empty field!!!")
    elif city_var.get() == "Select City" or state_var.get() == "Select State":
        error_label.config(text="fill the empty field!!!")
    else:
        error_label.config(text="")
        messagebox.showinfo("Success", "Registered Successfully!")



root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.config(bg="white")



name_var = tk.StringVar()
contact_var = tk.StringVar()
email_var = tk.StringVar()
gender_var = tk.StringVar()
city_var = tk.StringVar()
state_var = tk.StringVar()



top_label = tk.Label(root, text="Please enter details below", bg="orange", fg="white", font=("Arial", 12, "bold"))
top_label.pack(fill=tk.X)


form_frame = tk.Frame(root, bg="white", padx=20, pady=10)
form_frame.pack()



tk.Label(form_frame, text="Name *", bg="white").grid(row=0, column=0, sticky="w")
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1)


tk.Label(form_frame, text="Contact *", bg="white").grid(row=1, column=0, sticky="w")
tk.Entry(form_frame, textvariable=contact_var).grid(row=1, column=1)


tk.Label(form_frame, text="Email *", bg="white").grid(row=2, column=0, sticky="w")
tk.Entry(form_frame, textvariable=email_var).grid(row=2, column=1)


tk.Label(form_frame, text="Gender *", bg="white").grid(row=3, column=0, sticky="w")
gender_frame = tk.Frame(form_frame, bg="white")
gender_frame.grid(row=3, column=1)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="white").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="white").pack(side=tk.LEFT)


tk.Label(form_frame, text="City *", bg="white").grid(row=4, column=0, sticky="w")
ttk.Combobox(form_frame, textvariable=city_var, values=["ahemdabad", "Mumbai", "vadodara", "rajkot"]).grid(row=4, column=1)


tk.Label(form_frame, text="State *", bg="white").grid(row=5, column=0, sticky="w", pady=2)
ttk.Combobox(form_frame, textvariable=state_var, values=["gujrat", "Delhi", "uttarakhand", "himachal"]).grid(row=5, column=1)


error_label = tk.Label(form_frame, text="", fg="red", bg="white", font=("Arial", 10, "bold"))
error_label.grid(row=6, column=0, columnspan=2)


tk.Button(root, text="Register", bg="orange", fg="black", font=("Arial", 10, "bold"), command=register).pack(pady=10)

root.mainloop()