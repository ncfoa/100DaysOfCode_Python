from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_driver_path = "../../chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
cookie = driver.find_element_by_id("bigCookie")
items = driver.find_elements_by_css_selector("#store div .product")
item_ids = [item.get_attribute("id") for item in items]
acknowledge = driver.find_element_by_link_text("Got it!")
acknowledge.click()
end = time.time() + 60*30

def start():
    start_time = time.time()
    while time.time() - start_time < 20:
        cookie.click()
    check_items()

def check_items():
    global item_ids
    cookies = driver.find_element_by_css_selector("div #sectionLeft #cookies")
    cookies_txt = str(cookies.text)
    cookies_list = cookies_txt.split("\n")
    cookies_list = cookies_list[0].split(" ")
    cookies = cookies_list[0]

    cookies = cookies.replace(",", "")
    cookies = int(cookies)


    # Get all upgrade <b> tags
    all_prices = driver.find_elements_by_css_selector("#store .price")
    item_prices = []

    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        if "million" in element_text:
            element_text = element_text.strip().replace("million", "")
            element_text = str(int(float(element_text) * 1000000))
        if element_text != "":
            cost = int(element_text.strip().replace(",", ""))
            item_prices.append(cost)

    # Create dictionary of store items and prices
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if cookies > cost:
            affordable_upgrades[cost] = id

    # Purchase the most expensive affordable upgrade
    highest_price_affordable_upgrade = max(affordable_upgrades)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

    driver.find_element_by_id(to_purchase_id).click()
    if time.time() > end:
        cps = driver.find_element_by_css_selector("div #sectionLeft #cookies").text
        cps = cps.split("\n")

        print(f'Cookies {cps[1]}')
        driver.close()
        driver.quit()
        quit(0)
    else:
        start()

start()
