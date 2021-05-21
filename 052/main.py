from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CONFIG = dotenv_values(".env")



class InstaFollower:

    def __init__(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs",
                                       {"profile.default_content_setting_values.notifications": 2
                                        })
        self.chrome_driver_path = "../chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=option)
        self.username = CONFIG["IN_LOGIN"]
        self.password = CONFIG["IN_PASSWD"]
        self.similar_account = "wearecurated"

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_name("password").submit()

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{self.similar_account}")

        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
