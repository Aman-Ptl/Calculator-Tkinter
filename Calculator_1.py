# step 1:

from tkinter import *

#step 2: gui interaction

window =Tk()
window.geometry('500x500')

# step 3: adding inputs

#Entry Box

e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

#Buttons
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

b=Button(window, text="1", width=12, command=lambda:click(1))
b.place(x=10,y=60)
b=Button(window, text="2", width=12, command=lambda:click(2))
b.place(x=80,y=60)
b=Button(window, text="3", width=12, command=lambda:click(3))
b.place(x=150,y=60)
b=Button(window, text="4", width=12, command=lambda:click(4))
b.place(x=10,y=120)
b=Button(window, text="5", width=12, command=lambda:click(5))
b.place(x=80,y=120)
b=Button(window, text="6", width=12, command=lambda:click(6))
b.place(x=150,y=120)
b=Button(window, text="7", width=12, command=lambda:click(7))
b.place(x=10,y=180)
b=Button(window, text="8", width=12, command=lambda:click(8))
b.place(x=80,y=180)
b=Button(window, text="9", width=12, command=lambda:click(9))
b.place(x=150,y=180)

b=Button(window, text="0", width=12, command=lambda:click(0))
b.place(x=80,y=240)

# OPERATORS:
def sub():
    n1=e.get()
    global math
    math= "Substraction"
    global i
    i=int(n1)
    e.delete(0,END)

b=Button(window, text="-", width=12, command = sub)
b.place(x=10,y=240)
def add():
    n1=e.get()
    global math
    math = "Addition"
    global i
    i=int(n1)
    e.delete(0,END)
b=Button(window, text="+", width=12, command= add)
b.place(x=150,y=240)
def div():
    n1=e.get()
    global math
    math = "Division"
    global i
    i=int(n1)
    e.delete(0,END)
b=Button(window, text="/", width=12, command= div)
b.place(x=10,y=300)
def mult():
    n1=e.get()
    global math
    math = "Multiplication"
    global i
    i=int(n1)
    e.delete(0,END)
b=Button(window, text="*", width=12, command=mult)
b.place(x=80,y=300)

def modulus():
    n1=e.get()
    global math
    math = "Modulus"
    global i
    i=int(n1)
    e.delete(0,END)
b=Button(window, text="%", width=12, command=modulus)
b.place(x=150,y=300)

def pow():
    n1=e.get()
    global math
    math = "Power"
    global i
    i=int(n1)
    e.delete(0,END)
b=Button(window, text="pow", width=12, command=pow)
b.place(x=10,y=360)

def equal():
    n2=int(e.get())
    e.delete(0,END)
    if math=="Addition":
        e.insert(0,i + n2)
    elif math=="Substraction":
        e.insert(0,i - n2)
    elif math == "Multiplication":
        e.insert(0, i * n2)
    elif math == "Division":
        e.insert(0,i / n2)
    elif math == "Modulus":
        e.insert(0, i % n2)
    elif math == "Power":
        e.insert(0, i ** n2)

b=Button(window, text="=", width=12, command=equal)
b.place(x=80,y=360)

def clear():
    e.delete(0, END)

b=Button(window, text="clear", width=12, command= clear)
b.place(x=150,y=360)
#Step 4: main loop
mainloop()