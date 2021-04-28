import smtplib
import datetime as dt
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import random
from email.message import EmailMessage


MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "587"
CONFIG = dotenv_values(".env")


def send_mail(body_quote):
    to = CONFIG["TO"]  # Change to your email address to properly send mails
    body = f"R2 thinks you could probably use this... \n\n {body_quote}\n\n"
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Monday Motivation"
    msg['From'] = CONFIG["FROM"]
    msg['To'] = to

    with smtplib.SMTP(MAIL_SERVER, port=MAIL_PORT) as mail:
        mail.starttls()
        mail.login(user=CONFIG["FROM"], password=CONFIG["PASSWORD"])
        mail.send_message(msg)


def get_quote():
    with open("./quotes.txt", "r") as f:
        quotes = f.readlines()
        f.close()
    rand = random.randint(0, len(quotes) -1)
    return quotes[rand]


today = dt.datetime.now()
if today.weekday() == 0:
    quote = get_quote()
    send_mail(quote)
else:
    exit(0)
