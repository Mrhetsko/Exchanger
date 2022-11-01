import tkinter as tk
import tkinter.font as tkFont
from logic import logic


class App:
    # GUI
    def __init__(self, root):
        root.title("CZK Exchanger")
        width = 600
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.czk_to = tk.Label(root)
        self.czk_to["bg"] = "lightblue"
        ft = tkFont.Font(family='Times', size=10)
        self.czk_to["font"] = ft
        self.czk_to["fg"] = "#333333"
        self.czk_to["justify"] = "center"
        self.czk_to["text"] = "CZK to:"
        self.czk_to.place(x=70, y=15, width=70, height=25)

        self.toggle_btn = tk.Button(root)
        self.toggle_btn["bg"] = "gray"
        ft = tkFont.Font(family='Times', size=10)
        self.toggle_btn["font"] = ft
        self.toggle_btn["fg"] = "#000000"
        self.toggle_btn["justify"] = "center"
        self.toggle_btn["text"] = "Naopak"
        self.toggle_btn.place(x=290, y=10, width=60, height=20)
        self.toggle_btn["command"] = self.toggle_btn_command

        self.to_usd_btn = tk.Button(root)
        self.to_usd_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',  size=10)
        self.to_usd_btn["font"] = ft
        self.to_usd_btn["fg"] = "#000000"
        self.to_usd_btn["justify"] = "center"
        self.to_usd_btn["text"] = "USD"
        self.to_usd_btn.place(x=70, y=50, width=70, height=25)
        self.to_usd_btn["command"] = self.to_usd_btn_command

        self.to_eur_btn = tk.Button(root)
        self.to_eur_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.to_eur_btn["font"] = ft
        self.to_eur_btn["fg"] = "#000000"
        self.to_eur_btn["justify"] = "center"
        self.to_eur_btn["text"] = "EUR"
        self.to_eur_btn.place(x=70, y=80, width=70, height=25)
        self.to_eur_btn["command"] = self.to_eur_btn_command

        self.to_huf_btn = tk.Button(root)
        self.to_huf_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.to_huf_btn["font"] = ft
        self.to_huf_btn["fg"] = "#000000"
        self.to_huf_btn["justify"] = "center"
        self.to_huf_btn["text"] = "HUF"
        self.to_huf_btn.place(x=70, y=110, width=70, height=25)
        self.to_huf_btn["command"] = self.to_huf_btn_command

        self.to_uah_btn = tk.Button(root)
        self.to_uah_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.to_uah_btn["font"] = ft
        self.to_uah_btn["fg"] = "#000000"
        self.to_uah_btn["justify"] = "center"
        self.to_uah_btn["text"] = "UAH"
        self.to_uah_btn.place(x=70, y=140, width=70, height=25)
        self.to_uah_btn["command"] = self.to_uah_btn_command

        self.to_hrk_btn = tk.Button(root)
        self.to_hrk_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.to_hrk_btn["font"] = ft
        self.to_hrk_btn["fg"] = "#000000"
        self.to_hrk_btn["justify"] = "center"
        self.to_hrk_btn["text"] = "HRK"
        self.to_hrk_btn.place(x=70, y=170, width=70, height=25)
        self.to_hrk_btn["command"] = self.to_hrk_btn_command

        self.Enter_field = tk.Entry(root)
        self.Enter_field["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.Enter_field["font"] = ft
        self.Enter_field["fg"] = "#333333"
        self.Enter_field["justify"] = "center"
        self.Enter_field["text"] = ""
        self.Enter_field.place(x=180, y=50, width=95, height=34)

        self.rezult = tk.Message(root)
        ft = tkFont.Font(family='Times', size=15)
        self.rezult["font"] = ft
        self.rezult["fg"] = "#333333"
        self.rezult["justify"] = "center"
        self.rezult["text"] = "***"
        self.rezult.place(x=180, y=150, width=200, height=100)

        self.vypocet_btn = tk.Button(root)
        self.vypocet_btn["bg"] = "#90f090"
        ft = tkFont.Font(family='Times', size=10)
        self.vypocet_btn["font"] = ft
        self.vypocet_btn["cursor"] = "exchange"
        self.vypocet_btn["fg"] = "#000000"
        self.vypocet_btn["justify"] = "center"
        self.vypocet_btn["text"] = "Výpočet"
        self.vypocet_btn.place(x=290, y=50, width=65, height=49)
        self.vypocet_btn["command"] = self.count_btn_command

        self.email_btn = tk.Button(root)
        self.email_btn["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times', size=10)
        self.email_btn["font"] = ft
        self.email_btn["fg"] = "#000000"
        self.email_btn["justify"] = "center"
        self.email_btn["text"] = ""    # Poslat \n na email
        self.email_btn.place(x=475, y=150, width=77, height=39)
        self.email_btn["command"] = self.email_btn_command

        self.GLabel_140 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_140["font"] = ft
        self.GLabel_140["fg"] = "#333333"
        self.GLabel_140["justify"] = "center"
        self.GLabel_140["text"] = "Množství"
        self.GLabel_140.place(x=190, y=20, width=70, height=25)

        # Enter user email field
        self.enter_mail = tk.Entry(root)
        self.enter_mail["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.enter_mail["font"] = ft
        self.enter_mail["fg"] = "#333333"
        self.enter_mail["justify"] = "center"
        self.enter_mail["text"] = "Entry"
        self.enter_mail.place(x=430, y=50, width=160, height=34)

        self.label_email = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "center"
        self.label_email["text"] = "Zadejte email"
        self.label_email.place(x=460, y=20, width=70, height=25)

        self.glabel_64 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.glabel_64["font"] = ft
        self.glabel_64["fg"] = "#333333"
        self.glabel_64["justify"] = "center"
        self.glabel_64["text"] = "|\n|\n|"
        self.glabel_64.place(x=477, y=90, width=70, height=50)

        self.sys_message = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        self.sys_message["font"] = ft
        self.sys_message["fg"] = "#333333"
        self.sys_message["justify"] = "center"
        self.sys_message["text"] = ".."
        self.sys_message.place(x=290, y=330, width=288, height=50)

    # ----------------------------------------------------------------------------------------- #

    def toggle_btn_command(self):
        logic.toggle()
        if logic.toggle_counter % 2 != 0:
            self.toggle_btn["bg"] = '#C8250E'
            self.czk_to["bg"] = '#C8250E'
            self.czk_to["text"] = "to: CZK"
        else:
            self.toggle_btn["bg"] = "lightblue"
            self.czk_to["bg"] = "lightblue"
            self.czk_to["text"] = "CZK to:"

    def to_usd_btn_command(self):
        self.to_usd_btn["bg"] = "lightblue"     # changes the visual part GUI - buttons color
        self.to_eur_btn["bg"] = self.to_huf_btn["bg"] = self.to_uah_btn["bg"] = self.to_hrk_btn["bg"] = "#f0f0f0"
        self.to_usd_btn.place(x=80, width=75)   # changes the visual part GUI - buttons size and position
        self.to_eur_btn.place(x=70, width=70)   # changes the visual part GUI
        self.to_huf_btn.place(x=70, width=70)   # changes the visual part GUI
        self.to_uah_btn.place(x=70, width=70)   # changes the visual part GUI
        self.to_hrk_btn.place(x=70, width=70)   # changes the visual part GUI

        logic.cash = 'usd'                      # sets currency type in logic.py
        result = logic.get_money(logic.cash)
        self.rezult["text"] = f'1 CZK is: {result} USD'   # display information GUI

    def to_eur_btn_command(self):
        self.to_eur_btn["bg"] = "lightblue"
        self.to_usd_btn["bg"] = self.to_huf_btn["bg"] = self.to_uah_btn["bg"] = self.to_hrk_btn["bg"] = "#f0f0f0"
        self.to_usd_btn.place(x=70, width=70)
        self.to_eur_btn.place(x=80, width=75)
        self.to_huf_btn.place(x=70, width=70)
        self.to_uah_btn.place(x=70, width=70)
        self.to_hrk_btn.place(x=70, width=70)

        logic.cash = 'eur'
        result = logic.get_money(logic.cash)
        self.rezult["text"] = f'1 CZK is: {result} EUR'

    def to_huf_btn_command(self):
        self.to_huf_btn["bg"] = "lightblue"
        self.to_usd_btn["bg"] = self.to_eur_btn["bg"] = self.to_uah_btn["bg"] = self.to_hrk_btn["bg"] = "#f0f0f0"
        self.to_huf_btn.place(x=80, width=75)
        self.to_usd_btn.place(x=70, width=70)
        self.to_eur_btn.place(x=70, width=70)
        self.to_uah_btn.place(x=70, width=70)
        self.to_hrk_btn.place(x=70, width=70)

        logic.cash = 'huf'
        result = logic.get_money(logic.cash)
        self.rezult["text"] = f'1 CZK is: {result} HUF'

    def to_uah_btn_command(self):
        self.to_uah_btn["bg"] = "lightblue"
        self.to_usd_btn["bg"] = self.to_eur_btn["bg"] = self.to_huf_btn["bg"] = self.to_hrk_btn["bg"] = "#f0f0f0"
        self.to_uah_btn.place(x=80, width=75)
        self.to_usd_btn.place(x=70, width=70)
        self.to_eur_btn.place(x=70, width=70)
        self.to_huf_btn.place(x=70, width=70)
        self.to_hrk_btn.place(x=70, width=70)

        logic.cash = 'uah'
        result = logic.get_money(logic.cash)
        self.rezult["text"] = f'1 CZK is: {result} UAH'

    def to_hrk_btn_command(self):
        self.to_hrk_btn["bg"] = "lightblue"
        self.to_usd_btn["bg"] = self.to_eur_btn["bg"] = self.to_huf_btn["bg"] = self.to_uah_btn["bg"] = "#f0f0f0"
        self.to_hrk_btn.place(x=80, width=75)
        self.to_uah_btn.place(x=70, width=70)
        self.to_usd_btn.place(x=70, width=70)
        self.to_eur_btn.place(x=70, width=70)
        self.to_huf_btn.place(x=70, width=70)

        logic.cash = 'hrk'
        result = logic.get_money(logic.cash)
        self.rezult["text"] = f'1 CZK is: {result} HRK'

    def get_amount(self):
        amount = self.Enter_field.get()
        if amount == '':                        # check if string is empty
            amount = float(1)                   # empty string is not possible convert to float type
        if float(amount) <= 0:
            self.rezult["text"] = "pouze kladna cisla"

        else:
            amount = float(self.Enter_field.get())
        return amount

    def count_btn_command(self):
        try:
            if logic.toggle_counter % 2 == 0:
                self.rezult["text"] = f'{self.get_amount()} CZK je ' \
                                      f'{logic.calculate(self.get_amount()).__round__(2)}' \
                                      f' {logic.cash.upper()}'
            else:
                self.rezult["text"] = f'{self.get_amount()} {logic.cash.upper()} je ' \
                                      f'{logic.calculate(self.get_amount()).__round__(2)} CZK'
            self.email_btn["text"] = "Poslat \n na email"
        except ValueError:
            self.rezult["fg"] = "red"
            self.rezult["text"] = 'Zadejte číslo'

    def get_email(self):
        return str(self.enter_mail.get())

    def email_btn_command(self):
        if logic.process_mail(self.get_email()) is not False:
            self.sys_message["text"] = f'Poslano na {self.get_email()}'
        else:
            self.sys_message["fg"] = "red"
            self.sys_message["text"] = f'Neplatný e-mail'


if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.mainloop()