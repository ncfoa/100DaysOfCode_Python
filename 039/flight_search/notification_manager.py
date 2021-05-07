from twilio.rest import Client
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory

CONFIG = dotenv_values(".env")

TWILIO_ID = CONFIG["TWILIO_ID"]
TWILIO_KEY = CONFIG["TWILIO_KEY"]
TWILIO_FROM = CONFIG["TWILIO_FROM"]
TWILIO_TO = CONFIG["TWILIO_TO"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ID, TWILIO_KEY)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=TWILIO_TO,
        )
        # Prints if successfully sent.
        print(message.sid)
