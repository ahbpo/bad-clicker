#noni
#elikkä hommana ois tehä tämmöne nakutus peli

#imports
from tkinter import *
from tkinter import ttk

#vars
clicks = 0
cpc = 1

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("clicker")
        self.root.geometry("350x200")

        self.amount = ttk.Label(self.root, text=f"{clicks} clicks", font=26)
        self.amount.place(x=350/2, y=0)

        self.clicker = ttk.Button(self.root, text="small number\nget bigger", command=self.click)
        self.clicker.place(x=350/2.2, y=25)

        self.shopbutton = ttk.Button(self.root, text="shop", command=self.openshop)
        self.shopbutton.place(x=0, y=0)

        self.root.mainloop()

    def click(self):
        global clicks
        clicks += cpc
        self.amount.config(text=f"{clicks} clicks")

    def openshop(self):
        Shop()

class Shop:
    def __init__(self):
        self.shopwin = Toplevel()
        self.shopwin.title("shop")
        self.shopwin.geometry("300x200")

if __name__ == "__main__":
    Main()