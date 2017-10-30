from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class teamA:
    def __init__(self):
        window = Tk()
        window.title("Select your Team")
        window.minsize(width=300,height=300)
        window.configure(background='#00ffff')

        rm = Button(window, text="Real Madrid", command=self.openR).place(x=20, y=50)
        bar = Button(window, text="Barcelona", command=self.openB).place(x=150, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")
        import playerlistR

    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")
        import playerlistB

teamA()