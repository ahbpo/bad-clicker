#noni
#elikkä hommana ois tehä tämmöne nakutus peli

#imports
from tkinter import *
from tkinter import ttk

#vars
clicks = 0
cpc = 1

class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title("menu")
        self.root.geometry("300x200")

        self.button = ttk.Button(self.root, text="play da game", command=self.start)
        self.button.pack(pady=20)

        self.pressed = BooleanVar()
        self.check = ttk.Checkbutton(self.root, text="enable rawdog", variable=self.pressed, command=self.checkpressed)
        self.check.pack(pady=20)

        self.button2 = ttk.Button(self.root, text="rawdog it", state=DISABLED, command=self.startsimple)
        self.button2.pack(pady=10)

        self.root.mainloop()

    def start(self):
        self.root.destroy()
        Main(mode="normal")

    def checkpressed(self):
        if self.pressed.get():
            self.button2.config(state=NORMAL)
        else:
            self.button2.config(state=DISABLED)

    def startsimple(self):
        self.root.destroy()
        Main(mode="simple")

class Main:
    def __init__(self, mode):
        self.mode = mode
        self.root = Tk()
        self.root.title("clicker")
        self.root.geometry("350x200")

        self.amount = ttk.Label(self.root, text=f"{clicks} clicks", font=26)
        self.amount.place(x=350/2, y=0)

        self.clicker = ttk.Button(self.root, text="small number\nget bigger", command=self.click)
        self.clicker.place(x=350/2.2, y=25)
        if self.mode == "normal":
            self.shopbutton = ttk.Button(self.root, text="shop", command=self.openshop)
            self.shopbutton.place(x=0, y=0)

        self.root.mainloop()

    def click(self):
        global clicks
        clicks += cpc
        self.updateclicks()

    def openshop(self):
        Shop(self)

    def updateclicks(self):
        global clicks
        self.amount.config(text=f"{clicks} clicks")

class Shop:
    def __init__(self, main_instance):
        self.main_instance = main_instance

        self.shopwin = Toplevel()
        self.shopwin.title("shop")
        self.shopwin.geometry("300x200")

        self.addclick = ttk.Button(self.shopwin, text="buy 1 click\n(15 clicks)", command=self.buyclick)
        self.addclick.place(x=150-30)

    def buyclick(self):
        global clicks
        global cpc
        if clicks >= 15:
            clicks -= 15
            self.main_instance.updateclicks()
            cpc += 1

if __name__ == "__main__":
    Menu()