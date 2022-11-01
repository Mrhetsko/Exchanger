import smtplib
from art import tprint
from email.mime.text import MIMEText


def send_mail(message, user_mail):
    try:
        server = smtplib.SMTP('smtp.seznam.cz', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('mrhetsko@seznam.cz', 'Marika235')
        msg = MIMEText(message)
        msg['Subject'] = 'Exchanger online'
        msg['From'] = 'mrhetsko@seznam.cz'
        msg['To'] = f'{user_mail}'
        server.sendmail('mrhetsko@seznam.cz', user_mail, msg.as_string())
        server.quit()
        tprint("Success", font="cybermedium")

    except Exception as e:
        print('An error was occurred during sending message. Try later please')
        print(e)


if __name__ == '__main__':
    tprint('Sender', font="cybermedum")
    send_mail('Hello. This is a test mail from Exchanger', 'mrhetsko@gmail.com')
