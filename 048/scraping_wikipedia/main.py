from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


chrome_driver_path = "../../chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
WebDriverWait(driver, 10)
data = driver.find_element_by_css_selector("[title^='Special:Statistics']")
print(data.text)
query = driver.find_element_by_name("search")
query.send_keys("firefly tv show")
query.submit()

