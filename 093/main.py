from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://firefly.fandom.com/wiki/Quotes'
chrome_driver_path = '../chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

with driver as d:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # Retrieve url in headless browser
    driver.get(url)

    html = driver.page_source

    driver.close()
    driver.quit()

s = BeautifulSoup(html, "html.parser")
data = s.find_all("p")
quotes = [quote.getText() for quote in data]
with open("./ffly-serenity_quotes.txt", "w") as f:
    for i in quotes:
        m = i
        f.write(m + "\n")
    f.close()
