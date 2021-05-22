from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
import pandas as pd
import requests
from bs4 import BeautifulSoup

CONFIG = dotenv_values(".env")


class ApartmentFinder:

    def __init__(self):
        self.url = CONFIG["ZILLOW_LINK"]
        self.link_list = []
        self.address_list = []
        self.price_list = []
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8, application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/90.0.4430.93 Safari/537.36",
        }

    def scrape_zillow(self):

        resp = requests.get(self.url, headers=self.headers).text
        s = BeautifulSoup(resp, "html.parser")
        links = s.select(".list-card-top a")
        addresses = s.select(".list-card-info address")
        prices = s.select(".list-card-price")
        for link in links:
            if "zillow" not in link["href"]:
                self.link_list.append(f'https://www.zillow.com{link["href"]}')
            else:
                self.link_list.append(link["href"])
        for address in addresses:
            self.address_list.append(address.text)
        for price in prices:
            if "+" in price.text:
                price = price.text.split("+")
                self.price_list.append(price[0])
            elif "/" in price.text:
                price = price.text.split("/")
                self.price_list.append(price[0])
            elif " " in price.text:
                price = price.text.split(" ")
                self.price_list.append(price[0])
            else:
                self.price_list.append(price.text)

    def parse_to_csv(self):
        listings_dict = {"Price": self.price_list, "Address": self.address_list, "Link Url": self.link_list}
        df = pd.DataFrame(data=listings_dict).to_csv()
        with open("./listings.csv", "w") as fw:
            fw.write(df)
            fw.close()


bot = ApartmentFinder()
bot.scrape_zillow()
print(len(bot.price_list))
bot.parse_to_csv()
