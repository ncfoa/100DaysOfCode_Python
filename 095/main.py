import requests
import smtplib
import json
from datetime import datetime as dt
from dotenv import dotenv_values  # From address and password is held in a .env file in the directory
from email.message import EmailMessage


MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "587"
config = dotenv_values(".env")


def get_sites():
    with open("./sites_to_check.json", "r") as f:
        data = json.load(f)
        return data


def send_mail(site, status, date):
    letter = f"\n{date}\n\nWebsite {site} is unreachable with status code {status}.\n Please manually verify and resolve any issues. \n \n --Python_Dave"
    msg = EmailMessage()
    msg.set_content(letter)
    msg["Subject"] = "Website Down"
    msg['From'] = config["FROM"]
    msg['To'] = config["TO"]

    with smtplib.SMTP(MAIL_SERVER, port=MAIL_PORT) as mail:
        mail.starttls()
        mail.login(user=config["FROM"], password=config["PASSWORD"])
        mail.send_message(msg)


def check_sites():
    sites_to_check = get_sites()
    for i in sites_to_check:
        resp = requests.get(i)
        if resp.status_code != 300:
            date = dt.now()
            send_mail(site=i, status=resp.status_code, date=date)


if __name__ == '__main__':
    check_sites()
