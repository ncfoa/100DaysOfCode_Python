import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory

CONFIG = dotenv_values(".env")



def send_mail():
    from_addy = CONFIG["FROM"]
    to_addy = CONFIG["TO"]
    body = f"The item you were watching {URL} has dropped from ${my_price} to ${buy_price}"
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Amazon Product Price Alert"
    msg['From'] = from_addy
    msg['To'] = to_addy

    with smtplib.SMTP(CONFIG["MAIL_SERVER"], port=CONFIG["MAIL_PORT"]) as mail:
        mail.starttls()
        mail.login(user=CONFIG["FROM"], password=CONFIG["PASSWORD"])
        mail.send_message(msg)


URL = "https://amazon.com/Philips-HD9650-96-TurboStar-Technology/dp/B07G3V9K17/ref=sr_1_" \
      "4?dchild=1&keywords=philips+digital+air+fryer&qid=1620042759&sr=8-4"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8, "
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.93 Safari/537.36",
}

resp = requests.get(URL, headers=headers).text
s = BeautifulSoup(resp, "html.parser")
price = s.find("span", id="newBuyBoxPrice")

my_price = "{:.2f}".format(300.00)
buy_price = price.getText().split("$")
buy_price = "{:.2f}".format(float(buy_price[1]))

if buy_price < my_price:
    send_mail()






