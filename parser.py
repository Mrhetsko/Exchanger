import requests
import bs4
from art import tprint

# User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


class Currency:

    def __init__(self, currency=None):
        self.currency = currency
        self.headers = headers
        self.page = None
        self.my_currency = {
            'usd': 'https://www.google.com/search?q=koruna+k+dollaru&sxsrf=ALiCzsZY-oWspu8v_GD936rQ4-ZUn84hXQ%3A1654518371614&ei=Y_KdYuODJZ6Oxc8P2eaR0Aw&oq=koruna+k+doll&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQHhAWOgcIABBHELADSgQIQRgASgQIRhgAUK0JWK0JYL4TaAFwAXgAgAG9AYgBvQGSAQMwLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz',
            'huf': 'https://www.google.com/search?q=%D0%BA%D1%80%D0%BE%D0%BD%D0%B0+%D0%BA+forint&sxsrf=ALiCzsbwRyFU2_XqQ23FV_xomPDBoeNJFw%3A1654518444501&ei=rPKdYriMHt2Sxc8P3e2_4AI&ved=0ahUKEwi4kqLB6Zj4AhVdSfEDHd32DywQ4dUDCA4&uact=5&oq=%D0%BA%D1%80%D0%BE%D0%BD%D0%B0+%D0%BA+forint&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEB4QFhAKECoyCggAEB4QDxAWEAo6BwgAEEcQsAM6BAgjECc6BQgAEMsBOgQIABANOgYIABAeEBY6CAgAEB4QFhAKOgUIIRCgAUoECEEYAEoECEYYAFCgCFihL2DvMmgCcAF4AIAB6QGIAY8JkgEFMC42LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz',
            'eur': 'https://www.google.com/search?q=koruna+k+euro&oq=koruna+k+euro&aqs=chrome..69i57.5933j0j4&sourceid=chrome&ie=UTF-8',
            'uah': 'https://www.google.cz/search?q=czk+to+uah&rlz=1C1SQJL_ruUA817UA819&sxsrf=ALiCzsbvih1SDdH0cPPfR7KOKphwoGDdSA%3A1656620838140&ei=Jge-YpSICIqGxc8PzducqAM&oq=czk+to&gs_lcp=Cgdnd3Mtd2l6EAMYAzIJCCMQJxBGEIICMgQIIxAnMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywE6BwgAEEcQsAM6BwgAELADEEM6EgguEMcBENEDEMgDELADEEMYAToSCC4QxwEQowIQyAMQsAMQQxgBOgsILhCABBDHARCjAjoFCAAQgAQ6CwguEIAEEMcBENEDOgQILhBDOgQIABBDOggILhCABBDUAjoLCC4QgAQQxwEQrwFKBAhBGABKBAhGGABQmA9YnSJg4jtoAnABeACAAVeIAakDkgEBNpgBAKABAcgBDMABAdoBBAgBGAg&sclient=gws-wiz',
            'hrk': 'https://www.google.com/search?q=czk+to+hrk&oq=czk+to+hrk&aqs=chrome..69i57.7801j0j7&sourceid=chrome&ie=UTF-8',
            'gbp': 'https://www.google.com/search?q=czk+to+GBP&oq=czk+to+GBP&aqs=chrome..69i57.3912j0j7&sourceid=chrome&ie=UTF-8',
            'chf': 'https://www.google.com/search?q=czk+to+chf&oq=czk+to+chf&aqs=chrome..69i57.2895j0j7&sourceid=chrome&ie=UTF-8'
        }

    def set_currency(self, currency):
        self.currency = self.my_currency[currency]
        return self.currency                        # return currency's page ('usd'),, <class 'str'>

    def get_currency_value(self, page):                   # page = "usd", "eur" ...
        self.page = page
        self.headers = headers

        full_page = requests.get(self.set_currency(self.page), headers=self.headers)
        unordered_page = bs4.BeautifulSoup(full_page.content, 'html.parser')
        ordered_page = unordered_page.findAll(
            'span',
            {'class': ['DFlfde', 'SwHCTb'],
             'data-precision': [2, 3]}
        )

        value_string = ordered_page[0].text                                     # return string with ','
        value_float = float(value_string.replace(',', '.'))                     # string with '.'
        return value_float


my_money = Currency()

if __name__ == '__main__':
    tprint('parser inside', font="cybermedum")

    print(f" {my_money.get_currency_value('uah')} UAH")
    print(f" {my_money.get_currency_value('eur')} EUR")
    print(f" {my_money.get_currency_value('usd')} USD")
    print(f" {my_money.get_currency_value('hrk')} HRK")
    print(f" {my_money.get_currency_value('huf')} HUF")