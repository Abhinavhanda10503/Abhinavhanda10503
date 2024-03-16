import tkinter as tk
from tkinter import *
from tkinter.ttk import Radiobutton

root = tk.Tk()
root.title("Light")
root.configure(background="black")
root.geometry("500x250")
root.resizable(width=False, height=False)

def selection():
    s = int(var.get())
    if s == 1:
        entry1.configure(background="red")
        entry2.configure(background="white")
        entry3.configure(background="white")
    elif s == 2:
        entry1.configure(background="white")
        entry2.configure(background="green")
        entry3.configure(background="white")
    elif s == 3:
        entry1.configure(background="white")
        entry2.configure(background="white")
        entry3.configure(background="blue")
    elif s == 4:
        entry1.configure(background="red")
        entry2.configure(background="green")
        entry3.configure(background="blue")
    elif s == 5:
        def rtg():
            entry1.configure(background="white")
            entry2.configure(background="green")
            entry3.configure(background="white")
            root.after(1000, gtb)
        def gtb():
            entry1.configure(background="white")
            entry2.configure(background="white")
            entry3.configure(background="blue")
            root.after(1000, btr)
        def btr():
            entry1.configure(background="red")
            entry2.configure(background="white")
            entry3.configure(background="white")
            root.after(1000, rtg)
        btr()

var = tk.IntVar()

label1 = Label(root, text="Light", font=("Helvetica", 70), bg="black", fg="white")
label1.grid(row=0, column=0, columnspan=10, pady=20)  

entry1 = Entry(root, width=10)
entry1.grid(row=1, column=5, padx=20, pady=10)  

entry2 = Entry(root, width=10)
entry2.grid(row=1, column=6, padx=20, pady=10)

entry3 = Entry(root, width=10)
entry3.grid(row=1, column=7, padx=20, pady=10)

radio1 = Radiobutton(root, text="RED", variable=var, value=1, command=selection)
radio1.grid(row=2, column=4, padx=20, pady=5)  

radio2 = Radiobutton(root, text="Green", variable=var, value=2, command=selection)
radio2.grid(row=2, column=5, padx=20, pady=5)

radio3 = Radiobutton(root, text="Blue", variable=var, value=3, command=selection)
radio3.grid(row=2, column=6, padx=20, pady=5)

radio4 = Radiobutton(root, text="All", variable=var, value=4, command=selection)
radio4.grid(row=2, column=7, padx=20, pady=5)

radio5 = Radiobutton(root, text="Alt", variable=var, value=5, command=selection)
radio5.grid(row=2, column=8, padx=20, pady=5)

root.mainloop()