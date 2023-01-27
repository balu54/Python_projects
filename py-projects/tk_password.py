import tkinter as tk
import pass_gen as pas
from tkinter import *
pavan = tk.Tk()
la = Label(pavan, text="", font=("Ariel", 18))


def function():
        a = pas.my_gen()
        la.grid(row=2, column=0)
        la.config(text=f"{a}")


label = Label(pavan, text="Click The Button For Password", font=("Ariel",15)).grid(row=0,column=0)
button = Button(pavan,text="Click Here",command=function, font=("Ariel",15)).grid(row=1,column=0)
pavan.mainloop()