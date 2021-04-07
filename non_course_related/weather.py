import requests  # Requests is required to make http web calls to API
from dotenv import dotenv_values # API_KEY is held in a .env file in the directory
import json  # json.loads is required to convert the string data into JSON output

# Pull in the values from the .env file
config = dotenv_values(".env")

# sign up for a free account at https://www.weatherapi.com/  I may make this into a webpage scraper in the future.

# URL for API modified as an fstring to insert API_KEY
URL=f"http://api.weatherapi.com/v1/current.json?key={config['API_KEY']}&q=63031&aqi=no"
# Converting byte string to JSON
response = json.loads(requests.get(URL).content)
# Building a dictionary of required information for my purposes.
weather = {"location": response["location"]["name"] + "," + response["location"]["region"],
           "current_temp": str(response["current"]["temp_f"]) + "\xb0F",
           "current_conditions": response["current"]["condition"]["text"]}

# Print the info or return it or consume it however you want.
print(weather)



