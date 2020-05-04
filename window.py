from tkinter import *

def clicked(btn1, btn2, btn3):
    lbl.configure(text="Pressed Retire Now")
    btn1.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()
    print(selected.get())


window = Tk()

window.title("Financial Independence Calculator")

window.geometry('600x500')

lbl = Label(window, text="Welcome" )
lbl.grid(column=0, row=0)

selected = IntVar()

btn1 = Radiobutton( window, text="Retire NOW", value=1, variable=selected )
btn1.grid(column=0, row=1)

btn2 = Radiobutton( window, text="Retire at a specific age", value=2, variable=selected )
btn2.grid(column=1, row=1)

start_btn = Button( window, text="Go", command=lambda: clicked1(btn1, btn2, start_btn) )
start_btn.grid(column=2, row=1)




window.mainloop()