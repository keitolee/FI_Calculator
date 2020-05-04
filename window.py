from tkinter import *

def clicked1():
    lbl.configure(text="Pressed Retire Now")

def clicked2():
    lbl.configure(text="Pressed Retire at a specific age")

window = Tk()

window.title("Financial Independence Calculator")

window.geometry('600x500')

lbl = Label(window, text="Welcome" )
lbl.grid(column=0, row=0)

btn1 = Button( window, text="Retire NOW", command=clicked1 )
btn1.grid(column=0, row=1)

btn1 = Button( window, text="Retire at a specific age", command=clicked2 )
btn1.grid(column=1, row=1)

window.mainloop()