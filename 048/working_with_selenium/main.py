from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver_path = "../../chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://python.org")
WebDriverWait(driver, 10)
date = driver.find_elements_by_css_selector(".event-widget time")
items = driver.find_elements_by_css_selector(".event-widget li a")

event_dict = {}

for n in range(len(date)):
    event_dict[n] = {"date": date[n].text, "event": items[n].text}


print(event_dict)

driver.quit()

