import smtplib
import requests
import pytz
from datetime import datetime as dt
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from email.message import EmailMessage
from time import sleep

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "587"
CONFIG = dotenv_values(".env")
LAT = float(CONFIG["LAT"])
LNG = float(CONFIG["LNG"])


def send_mail():
    to = CONFIG["TO"]
    body = f"Watch out! \n\n The ISS is above you... \n\n Skynet is watching... "
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Skynet Tracking"
    msg['From'] = CONFIG["FROM"]
    msg['To'] = to

    with smtplib.SMTP(MAIL_SERVER, port=MAIL_PORT) as mail:
        mail.starttls()
        mail.login(user=CONFIG["FROM"], password=CONFIG["PASSWORD"])
        mail.send_message(msg)


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss = response.json()["iss_position"]

    if LAT - 5 <= float(iss["latitude"]) <= LAT + 5 and LNG - 5 <= float(iss["longitude"]) <= LNG + 5:
        return True


def is_night():
    parameters = {"lat": LAT, "lng": LNG, "formatted": 0}
    # Set time_zone to your local timezone
    time_zone = pytz.timezone('US/Central')
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    # gives sunrise and sunset in UTC
    sun_up = response.json()["results"]["sunrise"]
    sun_down = response.json()["results"]["sunset"]
    # sunrise and sunset converted to timezone specified US/Central for me
    su_local = dt.fromisoformat(sun_up).astimezone(time_zone)
    sd_local = dt.fromisoformat(sun_down).astimezone(time_zone)
    # Pull out only the hour of each date/time string
    su = str(su_local).split(" ")[1].split(":")[0]
    sd = str(sd_local).split(" ")[1].split(":")[0]

    now = dt.now().hour
    sunrise = int(su)
    sunset = int(sd)
    if now >= sunrise or now <= sunset:
        return True


while True:
    sleep(60)
    if is_night() and is_iss_overhead():
        send_mail()
