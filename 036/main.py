from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import requests
from twilio.rest import Client
from datetime import datetime, timedelta
import math

CONFIG = dotenv_values(".env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
NEWS_API = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": CONFIG["ALPHAVANTAGE_KEY"]
}
response = requests.get(url=STOCK_API, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_value = float(data_list[0]["4. close"])
day_before_value = float(data_list[1]["4. close"])
difference = abs(yesterday_value - day_before_value)
diff_percent = abs(difference / yesterday_value * 100)

yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
if diff_percent > 5:
    news_params = {
        "qinTitle": "Tesla",
        "from": yesterday,
        "sortBy": "relevancy",
        "apiKey": f'{CONFIG["NEWS_API_KEY"]}'
    }

    response = requests.get(NEWS_API, params=news_params)
    response.raise_for_status()
    news_data = response.json()["articles"]
    articles = news_data[:3]

if yesterday_value > day_before_value:
    intro = f' TSLA:🔺 + {str(math.floor(diff_percent))}'
else:
    intro = f' TSLA: 🔻 + {str(math.floor(diff_percent))} '

headlines = [f'\n {intro} \nHeadline: {article["title"]}\n Brief: {article["description"]}' for article in articles]
for headline in headlines:
    client = Client(CONFIG["TWILIO_ID"], CONFIG["TWILIO_KEY"])
    message = client.messages.create(body=headline, from_=str(CONFIG["TWILIO_FROM"]), to=f'{CONFIG["TWILIO_TO"]}')
