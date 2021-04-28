import json
import smtplib
from datetime import datetime as dt
from random import randint
from dotenv import dotenv_values  # From address and password is held in a .env file in the directory
from email.message import EmailMessage


MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "587"
config = dotenv_values(".env")
letters = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt" ]


def send_mail(letter, email):
    to = email
    msg = EmailMessage()
    msg.set_content(letter)
    msg["Subject"] = "Happy Birthday"
    msg['From'] = config["FROM"]
    msg['To'] = to

    with smtplib.SMTP(MAIL_SERVER, port=MAIL_PORT) as mail:
        mail.starttls()
        mail.login(user=config["FROM"], password=config["PASSWORD"])
        mail.send_message(msg)


def check_birthday():
    with open("./birthdays.json", "r") as f:
        data = json.load(f)
        f.close()
    today = dt.now()
    for i in data:
        if int(i["birthday"]["month"]) == today.month and int(i["birthday"]["day"]) == today.day:
            letter = letters[randint(0, len(letters) - 1)]
            with open(letter, "r") as ltr:
                letter = ltr.readlines()
                ltr.close()

            greeting = letter[0].replace('Hey [NAME],\n', f'Hey {i["name"]}, \n\n')
            letter.pop(0)
            letter[0] = greeting
            letter = " ".join(letter)
            send_mail(letter, i["email"])


check_birthday()
