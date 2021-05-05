import requests
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import json
from datetime import datetime as dt

CONFIG = dotenv_values(".env")

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": CONFIG["NUTRITIONIX_APPID"],
    "x-app-key": CONFIG["NUTRITIONIX_KEY"]
}
workout = input("What kind of workout did you do today? ")
body = {
 "query": workout,
 "gender": "male",
 "weight_kg": 97,
 "height_cm": 172.7,
 "age": 45
}

response = requests.post(url=NUTRITIONIX_URL, json=body, headers=headers)
results = response.json()

d = dt.now()
date = str(d.date())
time = str(d.time()).split(".")[0]

SHEETY_URL = "https://api.sheety.co/4ccacf88151baa2fd8482e0aa4cf7af6/myWorkouts/workouts"

sheety_headers = {
    "Authorization": f"Bearer {CONFIG['SHEETY_BEARER']}"
}

for exercise in results["exercises"]:
    sheety_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=SHEETY_URL, json=sheety_body, headers=sheety_headers)
print(sheety_response.content)