import random
from tkinter import *

class DiceRoller (object):

    def _init_(self, master):
       frame = Frame(master)
       frame.pack()
       self.label = label(master, font=("times", 200))
       button = button(master,text="Rolar dados", command=self.roll)
       button.place(x=200, y=0)

    def roll(self):
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(text=f"{random.choice(symbols)}{random.choice(symbols)}")
        self.label.pac()


if __name__=="_main_":
    root = Tk()
    root.title("jogo de dados")
    root.geometry("500x300")
    DiceRoller(root)
    root.mainloop()