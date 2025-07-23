import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("My First GUI")  
window.geometry("400x600") 
window.config(bg="gray")

"""tkinter.Label(text="firstname:").place(x=0, y=0)
tkinter.Label(text="lastname:").place(x=0, y=30)"""

tkinter.Label(text="firstname:",bg='lightblue',fg='brown',font='elephant 15').grid(row=0, column=0)
tkinter.Label(text="lastname:",bg='lightblue',fg='brown', font='elephant 15').grid(row=1, column=0)

fnm=tkinter.Entry()
fnm.grid(row=0, column=1)
lnm=tkinter.Entry()
lnm.grid(row=1, column=1)

"""tkinter.Radiobutton(Value=0,text="male",bg='lightblue',fg='brown',font='dubai 15 bold').grid(row=2, column=0)
tkinter.Radiobutton(Value=0,text="female",bg='lightblue',fg='brown',font='dubai 15 bold').grid(row=2, column=1)"""

tkinter.Radiobutton(text="Male").grid(row=2, column=0, sticky='w')
tkinter.Radiobutton(text="female").grid(row=2, column=1, sticky='w')

tkinter.Checkbutton(text="I agree to the terms and conditions", bg='lightblue', fg='brown', font='dubai 15 bold').grid(row=3, columnspan=2)


contrys = ['India', 'USA', 'UK', 'Canada', 'Australia']
ttk.Combobox(values=contrys).grid(row=4, column=0)

def btn_click():
    """print("Button clicked!")"""
    print("firstname:", fnm.get())
    print("lastname:", lnm.get())

tkinter.Button(text="Submit", bg='lightblue', fg='brown', font='dubai 15 bold').grid(row=5, columnspan=2) 




window.mainloop()