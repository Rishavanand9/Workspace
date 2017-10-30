from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox




class fifa:
    def __init__(self):
        window = Tk()
        window.title("Enter id & Password ")
        window.minsize(width=300,height=300)
        window.configure(background='black')

        l1 = Label(window, text="Username: ").place(x=10,y=10)
        l2 = Label(window, text="Password: ").place(x=10,y=50)
        self.n=StringVar()
        name = Entry(window,textvariable=self.n).place(x=100,y=10)
        self.p=StringVar()
        paswd = Entry(window,textvariable=self.p).place(x=100,y=50)
        log = Button(window, text="Log In",command=self.enter).place(x=50,y=100)


        window.mainloop()

    def enter(self):
        if self.n.get()=='rishav' or self.n.get()=='shailesh' and self.p.get()=='123' or self.p.get()=='000':
            tkMessageBox.showinfo("prompt","Welcome Mr "+self.n.get())
            import legues
        else:
            tkMessageBox.showinfo("prompt","Unauthorized Entry")


fifa()