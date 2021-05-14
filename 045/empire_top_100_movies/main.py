from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://www.empireonline.com/movies/features/best-movies-2'
chrome_driver_path = '../../chromedriver'

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
data = s.find_all("h3", class_="jsx-4245974604")
movies = [movie.getText() for movie in data]
movies.reverse()
with open("./movies.txt", "w") as f:
    for i in movies:
        if i == 'The Godfather':
            print(i)
            m = f'1) {i}'
            print(m)
        else:
            m = i
        f.write(m + "\n")
    f.close()
