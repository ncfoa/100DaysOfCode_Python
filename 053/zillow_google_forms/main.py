from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests
from bs4 import BeautifulSoup

CONFIG = dotenv_values(".env")

class ApartmentFinder:

    def __init__(self):
        self.url = CONFIG["ZILLOW_LINK"]
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8, application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/90.0.4430.93 Safari/537.36",
        }
        self.form_url = CONFIG["GOOGLE_FORM"]
        self.link_list = []
        self.address_list = []
        self.price_list = []
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs",
                                       {"profile.default_content_setting_values.notifications": 2
                                        })
        self.chrome_driver_path = "../../chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=option)

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

    def process_form(self):

        for i in range(len(self.price_list)):
            self.driver.get(self.form_url)
            sleep(5)
            self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.address_list[i])
            self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.price_list[i])
            self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.link_list[i])
            self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div').click()
        self.driver.close()
        self.driver.quit()


bot = ApartmentFinder()
bot.scrape_zillow()
bot.process_form()
