from selenium import webdriver
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


from time import sleep

CONFIG = dotenv_values(".env")
URL = "https://tinder.com"
chrome_driver_path = "../../chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=URL)
sleep(5)
# driver.maximize_window()
# Press login button
login_button = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
# Get rid of cookie banner

sleep(2)
# Login with facbook pop-up
driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
sleep(2)
driver.find_element_by_id("email").send_keys(CONFIG["EMAIL"])
driver.find_element_by_id("pass").send_keys(CONFIG["PASSWD"])
driver.find_element_by_id("pass").submit()
sleep(2)
# Return to main window
driver.switch_to.window(base_window)
# Get rid of useless pop-ups
sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]')

allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[2]/div/div/div[1]/button')
cookies.click()
print("Start sleep")
sleep(45)
print("end sleep")
like_you = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div[3]/button[2]')
like_you.click()
count = 0


def window_click():
    sleep(1)
    driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
    sleep(1)


def shut_down():
    driver.close()
    driver.quit()
    print(f"Swiped right on {count} profiles. Good Luck!")


for n in range(100):

    sleep(1)

    try:
        window_click()

    except ElementClickInterceptedException:
        print("errored")
        if driver.find_element_by_css_selector('# c-1903119181 > div > div > div.Bg\(\$green-gradient-radial\).CenterAlign.D\(f\).Fxd\(c\) > div.W\(100\%\).Ta\(c\).Mt\(24px\).Mt\(12px\)--s.Mt\(8px\)--xs > h3'):
            shut_down()
        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
        try:
            driver.find_element_by_xpath('//*[@id="c155633096"]/div/div/div[1]/div/div[4]/button').click()
        # Catch Add to home screen pop-up
        except NoSuchElementException:
            try:
                driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[2]/button[2]').click()
                window_click()

            except NoSuchElementException:
                sleep(2)
                window_click()
    # c-1903119181 > div > div > div.Bg\(\$green-gradient-radial\).CenterAlign.D\(f\).Fxd\(c\) > div.W\(100\%\).Ta\(c\).Mt\(24px\).Mt\(12px\)--s.Mt\(8px\)--xs > h3
    count += 1

shut_down()
