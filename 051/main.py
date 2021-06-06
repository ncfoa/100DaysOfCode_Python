from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CONFIG = dotenv_values(".env")


class AutomatedPost:

    def __init__(self):
        self.message = input("What would you like to post to Facebook and Twitter? ")
        self.fb_url = "https://m.facebook.com"
        self.fb_email = CONFIG["FB_EMAIL"]
        self.fb_password = CONFIG["FB_PASSWD"]
        self.twitter_url = "https://mobile.twitter.com"
        self.twitter_email = CONFIG["TW_EMAIL"]
        self.twitter_password = CONFIG["TW_PASSWD"]
        self.chrome_driver_path = "../chromedriver"

    def fb_post(self):

        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs",
                                       {"profile.default_content_setting_values.notifications": 2
                                        })
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=option)
        driver.get(self.fb_url)
        sleep(3)
        driver.find_element_by_name("email").send_keys(self.fb_email)
        driver.find_element_by_name("pass").send_keys(self.fb_password)
        sleep(1)
        driver.find_element_by_name("login").click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[1]/div/div/a').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div[3]/div/div/div[1]/div[2]').click()
        sleep(3)
        driver.find_element_by_class_name('composerInput').send_keys(self.message)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[3]/div/div/button').click()
        sleep(1)
        driver.close()
        driver.quit()

    def twitter_post(self):
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        driver.get(self.twitter_url)
        sleep(3)
        driver.find_element_by_link_text("Log in").click()
        sleep(1)
        driver.find_element_by_name("session[username_or_email]").send_keys(self.twitter_email)
        driver.find_element_by_name("session[password]").send_keys(self.twitter_password)
        driver.find_element_by_name("session[password]").submit()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(self.message)
        sleep(1)
        try:
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()
        except ElementClickInterceptedException:
            driver.find_element_by_xpath('//*[@id="react-root"]').send_keys(Keys.ESCAPE)
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()

        sleep(1)
        driver.close()
        driver.quit()


bot = AutomatedPost()
bot.fb_post()
bot.twitter_post()
# Please do not adjust your internets.. This is only a test. #Python
