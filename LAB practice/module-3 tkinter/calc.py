import tkinter

window=tkinter.Tk()
window.title("calc")  
window.geometry("400x600") 
window.config(bg="light pink")

tkinter.Label(text="Enter first number:",font="Elephant 10").grid(row=0,column=0)
tkinter.Label(text="Enter second number:",font="Elephant 10").grid(row=1,column=0)
fn=tkinter.Entry(font="Elephant 10")
fn.grid(row=0,column=1)
sn=tkinter.Entry(font="Elephant 10")
sn.grid(row=1,column=1)
def add():
    print("Addition:",int(fn.get())+int(sn.get()))
    
def sub():
    print("Subtraction:",int(fn.get())-int(sn.get()))
    
def mul():
    print("Multiplication:",int(fn.get())*int(sn.get()))
    
def div():
    print("Division:",int(fn.get())/int(sn.get()))

tkinter.Button(text="+",command=add,font="dubai 15").grid(row=2,column=0)
tkinter.Button(text="-",command=sub,font="dubai 15").grid(row=3,column=0)
tkinter.Button(text="*",command=mul,font="dubai 15").grid(row=4,column=0)
tkinter.Button(text="/",command=div,font="dubai 15").grid(row=5,column=0)


window.mainloop()