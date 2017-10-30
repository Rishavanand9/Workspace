from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class league:
    def __init__(self):
        window = Tk()
        window.minsize(width=300, height=300)
        window.title("SELECT YOUR LEAGUE")
        window.configure(background='yellow')

        l1 = Label(window, text="SELECT YOUR LEAGUE").place(x=50, y=10)
        b1 = Button(window, text="LA LIGA ", command=self.teamA).place(x=50, y=100)
        b2 = Button(window, text="BARCALAYS ", command=self.teamB).place(x=50, y=140)
        b3 = Button(window, text="BUNDESLIGA ", command=self.teamC).place(x=50, y=180)
        b4 = Button(window, text="SERIE A ", command=self.teamD).place(x=50, y=220)
        b5 = Button(window, text="VIEW ALL PLAYERS ", command=self.player).place(x=70, y=260)

        window.mainloop()

    def teamA(self):
        tkMessageBox.showinfo("prompt", "You have selected LaLiga")
        import teamA

    def teamB(self):
        tkMessageBox.showinfo("prompt", "You have selected EPL")
        import teamB

    def teamC(self):
        tkMessageBox.showinfo("prompt", "You have selected Bundesliga")
        import teamC

    def teamD(self):
        tkMessageBox.showinfo("prompt", "You have selected Serie A")
        import teamD

    def player(self):
        tkMessageBox.showinfo("prompt", "Opening PLayer list IN the database")
        import playerlist



league()