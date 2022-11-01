import re
import parser
import sender
import datetime as dt


class MyLogic:
    def __init__(self):
        self.toggle_counter = 0     # counter for "Naopak/Reverse" button
        self.temp = float(0)        # value of one single currency, for example: float 1.25
        self.cash = ''              # variable for currency type, for example: 'czk'
        self.message = ''           # email body content
        self.f_time = dt.datetime.now().strftime("%c")  # time of request

    def toggle(self):
        """Change toggle mode (GUI button 'Naopak')  ONLY FOR CLASSIC GUI"""
        self.toggle_counter += 1    # toggle_counter 0 = (CZK * USD); toggle_counter 1 = (CZK / USD) ...

    def get_money(self, cash: str):
        self.cash = cash

        result = str(parser.my_money.get_currency_value(self.cash))   # information for GUI
        self.temp = float(result)                     # value of one USD in float type for further calculations
        return result

    def calculate(self, amount):
        try:
            if self.toggle_counter % 2 == 0:
                total = float(amount * self.temp)
                self.message = f'{amount} CZK je {total.__round__(2)} {self.cash.upper()}\n' \
                               f'čas a datum: {self.f_time}\n' \
                               f'--------------------------------------'
                print(self.message)

            else:
                total = float(amount / self.temp)
                self.message = f'{amount} {self.cash.upper()} je {total.__round__(2)} CZK, \n' \
                               f'čas a datum: {self.f_time}\n' \
                               f'--------------------------------------'
                print(self.message)
            return total
        except TypeError:
            print('Only positive numbers')

    def process_mail(self, email):
        regex_patterns = '[a-zA-Z0-9]+@+[a-z]+\.+(com|net|cz|ua|org)'
        if re.search(regex_patterns, email):
            sender.send_mail(self.message, email)
            result = f'{email}'
            print(f'Poslano na {result}')
            return f'{email}'
        else:
            print('Neplatný e-mail')
            return False


logic = MyLogic()

if __name__ == '__main__':
    logic.toggle_counter = 1  # multiply

    print(logic.get_money('eur'))
    logic.calculate(100)
    # logic.process_mail('mrhetsko@gmail.com')

