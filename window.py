import tkinter as tk


LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


class FIapp(tk.Tk):

    def __init__( self, *args, **kwargs ):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = { }

        for i in (StartPage, RetireNow, RetireLater):

            frame = i(container, self)

            self.frames[i] = frame

            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Retire NOW", command=lambda: controller.show_frame(RetireNow))
        button1.pack()

        button2 = tk.Button(self, text="Retire at a Specific Date", command=lambda: controller.show_frame(RetireLater))
        button2.pack()


class RetireNow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "You Selected Retire Now", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self, text = "Please enter the following information:", font=MEDIUM_FONT)
        label1.pack()

        label2 = tk.Label(self, text = "Projected years of retirement", font=SMALL_FONT)
        label2.pack()
        txt1 = tk.Entry(self, width=10)
        txt1.pack()

        label3 = tk.Label(self, text = "Estimated monthly expenses", font=SMALL_FONT)
        label3.pack()
        txt2 = tk.Entry(self, width=10)
        txt2.pack()

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


class RetireLater(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "You Selected Retire Later", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        txt = tk.Entry(self, width=10)
        txt.pack()

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = FIapp()
app.mainloop()
