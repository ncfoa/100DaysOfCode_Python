import requests
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory

CONFIG = dotenv_values(".env")

SHEETY_ENDPOINT = f"https://api.sheety.co/{'EnterYourInfoHere'}"

sheety_headers = {
    "Authorization": f"Bearer {CONFIG['SHEETY_BEARER']}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
