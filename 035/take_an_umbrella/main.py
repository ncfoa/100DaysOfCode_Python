from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import requests
from twilio.rest import Client

CONFIG = dotenv_values(".env")
LAT = float(CONFIG["LAT"])
LNG = float(CONFIG["LNG"])

parameters = {
#     "lat": LAT,
#     "lon": LNG,
    "lat": 44.817619,
    "lon": -84.664230,
    "exclude": "minutely,current,daily",
    "units": "imperial",
    "appid": CONFIG["OPEN_WEATHER_KEY"]
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data["hourly"][:12]
hours_til_rain = 0
will_rain = False
will_snow = False
for i in weather_data:
    code = i["weather"][0]["id"]
    if 700 > code >= 600:
        will_snow = True
    elif code < 600:
        will_rain = True
from_number = CONFIG["TWILIO_FROM"]

if will_snow and will_rain:
    client = Client(CONFIG["TWILIO_ID"], CONFIG["TWILIO_KEY"])
    message = client.messages.create(body="Rain and Snow expected today, take proper precautions.",
                                     from_=str(CONFIG["TWILIO_FROM"]), to=f'{CONFIG["TWILIO_TO"]}')

    print(message.sid)
elif will_rain and not will_snow:
    client = Client(CONFIG["TWILIO_ID"], CONFIG["TWILIO_KEY"])
    message = client.messages.create(body="An umbrella may be needed today.",
                                     from_=f'{CONFIG["TWILIO_FROM"]}', to=f'{CONFIG["TWILIO_TO"]}')

elif will_snow and not will_rain:
    client = Client(CONFIG["TWILIO_ID"], CONFIG["TWILIO_KEY"])
    message = client.messages.create(body="Snowy conditions expected today, take proper precautions.",
                                     from_=f'{CONFIG["TWILIO_FROM"]}', to=f'{CONFIG["TWILIO_TO"]}')
    print(message.sid)


