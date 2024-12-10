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
        self.root.geometry("300x350")

        self.button = ttk.Button(self.root, text="play", command=self.start)
        self.button.pack(pady=20)

        self.pressed = BooleanVar()
        self.check = ttk.Checkbutton(self.root, text="enable hard mode", variable=self.pressed, command=self.checkpressed)
        self.check.pack(pady=20)

        self.button2 = ttk.Button(self.root, text="hard mode\n(no upgrades)", state=DISABLED, command=self.startsimple)
        self.button2.pack(pady=10)

        self.devon = BooleanVar()
        self.devmode = ttk.Checkbutton(self.root, text="enable dev mode", variable=self.devon)
        self.devmode.pack(pady=20)

        self.quit = ttk.Button(self.root, text="quit", command=self.exit)
        self.quit.pack(pady=20)

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

    def exit(self):
        Quit()

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
            self.shopbutton.place(x=5, y=0)

        self.cpclabel = ttk.Label(self.root, text="1 clicks per click\nx1 modifier")
        self.cpclabel.place(x=350/2.2, y=75)

        if self.dev:
            self.am = ttk.Entry(self.root)
            self.am.place(x=5, y=75)
            self.give = self.am.get()

            self.conf = ttk.Button(self.root, text="confirm", command=self.makeclicks)
            self.conf.place(x=5, y=100)

        self.returnmenu = ttk.Button(self.root, text="quit", command=self.exit)
        self.returnmenu.place(x=5, y=30)

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

    def exit(self):
        self.root.destroy()
        Menu()

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
        self.cpcprice = 15
        self.modprice = 1500
        self.pricemult = {"cpc":1.2, "mod":1.2}

        self.shopwin = Toplevel()
        self.shopwin.title("shop")
        self.shopwin.geometry("300x200")

        self.info = ttk.Button(self.shopwin, text="info", command=self.openinfo)
        self.info.place(x=0, y=0)

        self.addclick = ttk.Button(self.shopwin, text="buy 1 cpc\n(18 clicks)", command=self.buyclick)
        self.addclick.place(x=150-30)

        self.multiclick = ttk.Button(self.shopwin, text=f"buy 1 cpc modifier\n({self.modprice} clicks)", command=self.buymultclick)
        self.multiclick.place(x=150-30, y=45)

        self.updateprices()

    def buyclick(self):
        global clicks
        global cpc
        new_price = round(self.cpcprice * self.pricemult["cpc"])
        if clicks >= self.cpcprice:
            clicks -= self.cpcprice
            cpc += 1
            self.cpcprice = new_price
            self.main_instance.updateall()
            self.updateprices()

    def buymultclick(self):
        global modifier
        global clicks
        new_price = round(self.modprice * self.pricemult["mod"])
        if clicks >= self.modprice:
            clicks -= self.modprice
            modifier += 1
            self.modprice = new_price
            self.main_instance.updateall()
            self.updateprices()

    def openinfo(self):
        Info(self)

    def updateprices(self):
        self.addclick.config(text=f"buy 1 cpc\n({self.cpcprice} clicks)")
        self.multiclick.config(text=f"buy 1 cpc modifier\n({self.modprice} clicks)")

class Info:
    def __init__(self, shop_instance):
        self.shop_instance = shop_instance

        self.infowin = Toplevel(master=self.shop_instance.shopwin)
        self.infowin.title("info")

        self.info = ttk.Label(self.infowin, text="In the shop, you spend your hard-earned clicks, and gain clicks per clicks (cpc).\nCpc increases the amounts of clicks (currency) per every click (physical).")
        self.info.pack()

class Quit:
    def __init__(self):
        self.exitmenu = Toplevel()
        self.exitmenu.title("exit")
        self.exitmenu.geometry("200x150")

        self.sure = ttk.Label(self.exitmenu, text="Are you sure?\nProgress is not saved!")
        self.sure.grid(row=1, column=0)

        self.accept = ttk.Button(self.exitmenu, text="yes", command=self.yes)
        self.accept.grid(row=0, column=1)

        self.refuse = ttk.Button(self.exitmenu, text="no", command=self.no)
        self.refuse.grid(row=2, column=1)

        self.exitmenu.mainloop()

    def yes(self):
        exit()

    def no(self):
        self.exitmenu.destroy()

if __name__ == "__main__":
    Menu()