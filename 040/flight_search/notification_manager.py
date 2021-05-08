from twilio.rest import Client
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import smtplib
from email.message import EmailMessage

CONFIG = dotenv_values(".env")

TWILIO_ID = CONFIG["TWILIO_ID"]
TWILIO_KEY = CONFIG["TWILIO_KEY"]
TWILIO_FROM = CONFIG["TWILIO_FROM"]
TWILIO_TO = CONFIG["TWILIO_TO"]
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
FROM_ADDRESS = CONFIG["FROM"]
FROM_PASSWORD = CONFIG["FROM_PASS"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ID, TWILIO_KEY)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=TWILIO_TO,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=FROM_ADDRESS, password=FROM_PASSWORD)
            for email in emails:
                msg = EmailMessage()
                mail_data = f"{message}\n{google_flight_link}".encode('utf-8')
                msg.set_content(mail_data)
                msg["Subject"] = "New Low Price Flight!"
                msg['From'] = FROM_ADDRESS
                msg['To'] = email
                connection.send_message(msg)
