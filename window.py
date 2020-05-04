from tkinter import *

def clicked1(btn1, btn2):
    lbl.configure(text="Pressed Retire Now")
    btn1.grid_forget()
    btn2.grid_forget()


def clicked2(btn1, btn2):
    lbl.configure(text="Pressed Retire at a specific age")
    btn2.grid_forget()
    btn1.grid_forget()

window = Tk()

window.title("Financial Independence Calculator")

window.geometry('600x500')

lbl = Label(window, text="Welcome" )
lbl.grid(column=0, row=0)

btn1 = Button( window, text="Retire NOW", command=lambda: clicked1(btn1, btn2) )
btn1.grid(column=0, row=1)

btn2 = Button( window, text="Retire at a specific age", command=lambda: clicked2(btn2, btn1) )
btn2.grid(column=1, row=1)

window.mainloop()