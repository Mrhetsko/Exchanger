from logic import logic
import tkinter
import tkinter.messagebox
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{800}x{500}")
        self.title("CZK Exchanger")

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        # self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=10)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="CZK to :",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_eur = customtkinter.CTkButton(master=self.frame_left,
                                                  text="EUR",
                                                  width=65,
                                                  command=self.button_eur_event)
        self.button_eur.grid(row=2, column=0, pady=10, padx=10)

        self.button_usd = customtkinter.CTkButton(master=self.frame_left,
                                                  text="USD",
                                                  width=65,
                                                  command=self.button_usd_event)
        self.button_usd.grid(row=3, column=0, pady=10, padx=10)

        self.button_uah = customtkinter.CTkButton(master=self.frame_left,
                                                  text="UAH",
                                                  width=65,
                                                  command=self.button_uah_event)
        self.button_uah.grid(row=4, column=0, pady=10, padx=10)

        self.button_hrk = customtkinter.CTkButton(master=self.frame_left,
                                                  text="HRK",
                                                  width=65,
                                                  command=self.button_hrk_event)
        self.button_hrk.grid(row=5, column=0, pady=10, padx=10)

        self.button_huf = customtkinter.CTkButton(master=self.frame_left,
                                                  text="HUF",
                                                  width=65,
                                                  command=self.button_huf_event)
        self.button_huf.grid(row=6, column=0, pady=10, padx=10)

        self.button_chf = customtkinter.CTkButton(master=self.frame_left,
                                                  text="CHF",
                                                  width=65,
                                                  command=self.button_chf_event)
        self.button_chf.grid(row=7, column=0, pady=10, padx=10)

        self.button_gbp = customtkinter.CTkButton(master=self.frame_left,
                                                  text="GBP",
                                                  width=65,
                                                  command=self.button_gbp_event)
        self.button_gbp.grid(row=8, column=0, pady=10, padx=10)



        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Theme:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=0, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["System", "Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=0, padx=10, sticky="w")

        # ============ frame_right ============

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Good day to spend cash!)",
                                                   text_font="Bold",
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="Naopak",
                                                fg_color="gray38",
                                                command=self.switch_event)
        self.switch_1.grid(row=2, column=0, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=80,
                                            placeholder_text="Zadejte mnozstvy")
        self.entry.grid(row=3, column=0, columnspan=1, pady=20, padx=40, sticky="we")

        self.count_button = customtkinter.CTkButton(master=self.frame_right,
                                                    text="Vypocet",
                                                    width=100,
                                                    height=30,
                                                    command=self.count_btn_event)
        self.count_button.grid(row=3, column=1, columnspan=1, pady=10, padx=10)

        # =========mail===========

        self.email = tkinter.IntVar(value=0)

        self.label_email_zone = customtkinter.CTkLabel(master=self.frame_right,
                                                       text="Send to Email")
        self.label_email_zone.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.email_entry = customtkinter.CTkEntry(master=self.frame_right,
                                                  width=140,
                                                  placeholder_text="",)
        self.email_entry.grid(row=1, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.send_mail_btn = customtkinter.CTkButton(master=self.frame_right,
                                                     text="",
                                                     width=65,
                                                     height=50,
                                                     command=self.send_mail_event)
        self.send_mail_btn.grid(row=2, column=2, pady=10, padx=10)

        self.label_sys_message = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="",
                                                        height=100,
                                                        corner_radius=6,
                                                        fg_color=("white", "gray38"),
                                                        justify=tkinter.LEFT)
        self.label_sys_message.grid(row=3, column=2, sticky="nwe", padx=15, pady=15)

    def get_email(self):
        return str(self.email_entry.get())

    def send_mail_event(self):
        if logic.process_mail(self.get_email()) is not False:
            self.label_sys_message.configure(text=f'Poslano na \n{self.get_email()}')
        else:
            self.label_sys_message.configure(text_color='red')
            self.label_sys_message.configure(text=f'Neplatný e-mail')

    def switch_event(self):
        logic.toggle_counter = self.switch_1.get()
        if logic.toggle_counter == 1:
            self.label_1.configure(text='To CZK :')
        else:
            self.label_1.configure(text='CZK to :')
        print("switch toggled, current value:", self.switch_1.get())

    def button_eur_event(self):
        logic.cash = 'eur'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')
        print(result)

    def button_usd_event(self):
        logic.cash = 'usd'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')
        print(result)

    def button_uah_event(self):
        logic.cash = 'uah'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')
        print(result)

    def button_hrk_event(self):
        logic.cash = 'hrk'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')
        print(result)

    def button_huf_event(self):
        logic.cash = 'huf'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')
        print(result)

    def button_gbp_event(self):
        logic.cash = 'gbp'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')

    def button_chf_event(self):
        logic.cash = 'chf'
        result = logic.get_money(logic.cash)
        self.label_info_1.configure(text=f'1 CZK is: {result} {logic.cash.upper()}')

    def get_amount(self):
        amount = self.entry.get()
        if amount == '':                        # check if string is empty
            amount = float(1)                   # empty string is not possible convert to float type
        if float(amount) <= 0:
            self.label_info_1.configure(text = "pouze kladna cisla")

        else:
            amount = float(self.entry.get())
        return amount

    def count_btn_event(self):
        try:
            if logic.toggle_counter == 0:
                self.label_info_1.configure(text=f'{self.get_amount()} CZK je '
                                                 f'{logic.calculate(self.get_amount()).__round__(2)}'
                                                 f' {logic.cash.upper()}')
            else:
                self.label_info_1.configure(text=f'{self.get_amount()} {logic.cash.upper()} je '
                                                 f'{logic.calculate(self.get_amount()).__round__(2)} CZK')
            self.send_mail_btn.configure(text='Poslat na email')
            self.email_entry.configure(placeholder_text='Zadejte email')
        except ValueError:
            self.label_info_1.configure(text_color='red')
            self.label_info_1.configure(text='Zadejte číslo')

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()