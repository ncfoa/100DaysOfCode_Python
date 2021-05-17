import json
from selenium import webdriver
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from datetime import datetime as dt
from time import sleep

CONFIG = dotenv_values(".env")

URL = "https://www.linkedin.com/jobs/search/?currentJobId=2442922626&f_JT=F&f_WRA=true&geoId=103644278&keywords=" \
      "python%20developer&location=United%20States"

chrome_driver_path = "../../chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=URL)
sleep(3)
login_button = driver.find_element_by_link_text("Sign in")
login_button.click()
sleep(3)
driver.find_element_by_id("username").send_keys(CONFIG["LI_LOGIN"])
sign_in = driver.find_element_by_id("password").send_keys(CONFIG["LI_PSWD"])
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(3)
# driver.find_element_by_xpath('//button[text()="Not now"]').click()
# sleep(5)
jobs = driver.find_elements_by_css_selector("li.jobs-search-results__list-item")
jobs_dict = {}
idx = 0
for i in jobs:
    sleep(5)
    i.click()
    sleep(3)
    title = driver.find_element_by_class_name("jobs-details-top-card__job-title").text
    description = driver.find_elements_by_css_selector("div.jobs-description-content__text > span")
    for a in description:
        jobs_dict[idx] ={"title": title, "description": a.text}
    idx += 1


driver.close()
driver.quit()

now = dt.now().strftime("%Y_%m_%d_%H%M%S")
file = f' {now}_LinkedIn_Jobs.json'
with open(file, "w") as f:
    f.write(json.dumps(jobs_dict))
