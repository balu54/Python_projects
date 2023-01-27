from tkinter import *
import tkinter as tki
cal = Tk()
cal.title("calulator")
# cal.minsize(500,500)
# cal.maxsize(500,500)
entry = Entry(cal,width=80,borderwidth=6,font=("Ariel",20))
entry.grid(row=0,column=0,columnspan=4)
b11 = ""
def click(b):
    global b11
    a = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(a) + str(b))
    b11 = entry.get()

    return b11


def clear():

    entry.delete(0,END)


def equ():
    final = entry.get()
    entry.delete(0,END)
    global b11
    entry.insert(0,eval(b11))
    # if b11 =="add":
    #     entry.insert(0,(b11) + float(final))
    # elif b11 == "sub":
    #     entry.insert(0,(fnum) - float(final))
    # elif fnum =="mul":
    #     entry.insert(0,(fnum) * float(final))
    # elif fnum =="div":
    #     entry.insert(0,(fnum) / float(final))

b1 =Button(cal,padx=40,pady=20,command=lambda: click(1),width=20,height=5,text="1",font=("Ariel",15))
b2 =Button(cal,padx=40,pady=20,command=lambda: click(2),width=20,height=5,text="2",font=("Ariel",15))
b3 =Button(cal,padx=40,pady=20,command=lambda: click(3),width=20,height=5,text="3",font=("Ariel",15))
b4 =Button(cal,padx=40,pady=20,command=lambda: click(4),width=20,height=5,text="4",font=("Ariel",15))
b5 =Button(cal,padx=40,pady=20,command=lambda: click(5),width=20,height=5,text="5",font=("Ariel",15))
b6 =Button(cal,padx=40,pady=20,command=lambda: click(6),width=20,height=5,text="6",font=("Ariel",15))
b7 =Button(cal,padx=40,pady=20,command=lambda: click(7),width=20,height=5,text="7",font=("Ariel",15))
b8 =Button(cal,padx=40,pady=20,command=lambda: click(8),width=20,height=5,text="8",font=("Ariel",15))
b9 =Button(cal,padx=40,pady=20,command=lambda: click(9),width=20,height=5,text="9",font=("Ariel",15))
b0 =Button(cal,padx=40,pady=20,command=lambda: click(0),width=20,height=5,text="0",font=("Ariel",15))
b_plus =Button(cal,padx=40,pady=20,command=lambda:click("+"),text="+",width=20,height=5,font=("Ariel",15))
b_minus =Button(cal,padx=40,pady=20,command=lambda: click("-"),text="-",width=20,height=5,font=("Ariel",15))
b_mul =Button(cal,padx=40,pady=20,command=lambda: click("*"),text="*",width=20,height=5,font=("Ariel",15))
b_div =Button(cal,padx=40,pady=20,command=lambda: click("/"),text="/",width=20,height=5,font=("Ariel",15))
b_clear =Button(cal,padx=40,pady=20,command=clear,text="C",width=20,height=5,font=("Ariel",15))
b_equ =Button(cal,padx=40,pady=20,command=equ,text="=",width=20,height=5,font=("Ariel",15))
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=1)
b_plus.grid(row=4,column=3)
b_minus.grid(row=3,column=3)
b_mul.grid(row=2,column=3)
b_div.grid(row=1,column=3)
b_clear.grid(row=4,column=0)
b_equ.grid(row=4,column=2)
cal.mainloop()