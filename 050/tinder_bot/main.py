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
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[2]/div/div/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                             'div/div[2]/div[2]/a').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
sleep(2)
driver.find_element_by_id("email").send_keys(CONFIG["EMAIL"])
driver.find_element_by_id("pass").send_keys(CONFIG["PASSWD"])
driver.find_element_by_id("pass").submit()
# driver.find_element_by_name("__CONFIRM__").click()
sleep(2)
driver.switch_to.window(base_window)
count = 0
sleep(2)
driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[1]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[2]').click()
sleep(30)


def window_click():
    sleep(1)
    driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]'
                                 '/div[4]/button').click()


def shut_down():
    driver.close()
    driver.quit()
    print(f"Swiped right on {count} profiles. Good Luck!")


while (driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/'
                                    'div[2]/div[4]/button')):
    sleep(1)
    # driver.find_element_by_xpath('//*[@id="t1527440394"]/div/div/div[1]/div/div[4]/button').click()
    try:
        window_click()
        if driver.find_element_by_css_selector('h3.Fz($ms).Fw($semibold).C(#fff)').text == "Get Tinder Plus®":
            shut_down()
        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        print("errored")
        try:
            driver.find_element_by_xpath('//*[@id="t1527440394"]/div/div/div[1]/div/div[4]/button').click()
            print("try")
        # Catch Add to home screen pop-up
        except NoSuchElementException:
            try:
                print("first exception")
                driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[2]/button[2]').click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
            except NoSuchElementException:
                print("second exception")
                sleep(2)

    count += 1
