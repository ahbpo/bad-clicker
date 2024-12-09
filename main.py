#noni
#elikkä hommana ois tehä tämmöne nakutus peli

#imports
from tkinter import *
from tkinter import ttk

#vars
clicks = 0
cpc = 1
modifier = 1

class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title("menu")
        self.root.geometry("300x250")

        self.button = ttk.Button(self.root, text="play da game", command=self.start)
        self.button.pack(pady=20)

        self.pressed = BooleanVar()
        self.check = ttk.Checkbutton(self.root, text="enable hard mode", variable=self.pressed, command=self.checkpressed)
        self.check.pack(pady=20)

        self.button2 = ttk.Button(self.root, text="hard mode\n(no upgrades)", state=DISABLED, command=self.startsimple)
        self.button2.pack(pady=10)

        self.devon = BooleanVar()
        self.devmode = ttk.Checkbutton(self.root, text="enable dev mode", variable=self.devon)
        self.devmode.pack(pady=20)

        self.root.mainloop()

    def start(self):
        dev = self.devon.get()
        self.root.destroy()
        Main(mode="normal", dev=dev)

    def checkpressed(self):
        if self.pressed.get():
            self.button2.config(state=NORMAL)
        else:
            self.button2.config(state=DISABLED)

    def startsimple(self):
        dev = self.devon.get()
        self.root.destroy()
        Main(mode="simple", dev=dev)

class Main:
    def __init__(self, mode, dev):
        self.dev = dev
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

        self.cpclabel = ttk.Label(self.root, text="1 clicks per click\nx1 modifier")
        self.cpclabel.place(x=350/2.2, y=75)

        if self.dev:
            self.am = ttk.Entry(self.root)
            self.am.place(x=5, y=75)
            self.give = self.am.get()

            self.conf = ttk.Button(self.root, text="confirm", command=self.makeclicks)
            self.conf.place(x=5, y=100)

        self.root.mainloop()

    def click(self):
        global clicks
        global modifier
        global cpc

        if cpc < 1:
            cpc = 1
        elif modifier < 1:
            modifier = 1

        clicks += cpc * modifier
        self.updateclicks()

    def makeclicks(self):
        global clicks
        self.give = self.am.get()
        if self.give.isnumeric():
            clicks = int(self.give)
            self.updateclicks()

    def openshop(self):
        Shop(self)

    def updateclicks(self):
        global clicks
        self.amount.config(text=f"{clicks} clicks")

    def updatelabels(self):
        global cpc
        global modifier
        self.cpclabel.config(text=f"{cpc} clicks per click\nx{modifier} modifier")

    def updateall(self):
        self.updateclicks()
        self.updatelabels()


class Shop:
    def __init__(self, main_instance):
        self.main_instance = main_instance

        self.shopwin = Toplevel()
        self.shopwin.title("shop")
        self.shopwin.geometry("300x200")

        self.info = ttk.Button(self.shopwin, text="info", command=self.openinfo)
        self.info.place(x=0, y=0)

        self.addclick = ttk.Button(self.shopwin, text="buy 1 cpc\n(15 clicks)", command=self.buyclick)
        self.addclick.place(x=150-30)

        self.multiclick = ttk.Button(self.shopwin, text="buy 1 cpc modifier\n(1500 clicks)", command=self.buymultclick)
        self.multiclick.place(x=150-30, y=45)

    def buyclick(self):
        global clicks
        global cpc
        if clicks >= 15:
            clicks -= 15
            cpc += 1
            self.main_instance.updateall()

    def buymultclick(self):
        global modifier
        global clicks
        if clicks >= 1500:
            clicks -= 1500
            modifier += 1
            self.main_instance.updateall()

    def openinfo(self):
        Info(self)

class Info:
    def __init__(self, shop_instance):
        self.shop_instance = shop_instance

        self.infowin = Toplevel(master=self.shop_instance.shopwin)
        self.infowin.title("info")

        self.info = ttk.Label(self.infowin, text="In the shop, you spend your hard-earned clicks, and gain clicks per clicks (cpc).\nCpc increases the amounts of clicks (currency) per every click (physical).")
        self.info.pack()

if __name__ == "__main__":
    Menu()