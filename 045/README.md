# 100 Days of Code Python
## Day 45 of course. 

Website scraping using the BeautifulSoup python package.

### Course Deviation
The course centered around the [Empire](https://www.empireonline.com/movies/features/best-movies-2/) top 100 list. That site
has since then been rebuilt with React JS and required a different
solution to scrape with. Since this should have been a simple
scraping of a website, I then searched for other pages with 
lists of top100 movies. I came across [AFI](https://www.afi.com/afis-100-years-100-movies/)
I decided to try and scrape this site but that was a bust
due to Cloudflare's IUAM ("I'm Under Attack Mode"). I was able
to find a University's website that contains AFI's data at [GFU](https://www.georgefox.edu/library/explore-contribute/collections/afi-top100-films.html).
This allowed me to follow the prescribed path that the course
was taking but with a different dataset. 

#### What I did for afi_top_100_movies:
Just minor changes to the code to scrape the page and parse 
the content properly. Nothing major.

#### What I did for empire_top_100_movies:
This required a bit more. You need to `pip install selenium` 
for this page to work. You also need to download the [Chrome Web Driver](https://chromedriver.chromium.org/downloads)
for your OS and drop it into the directory. I was then able to
scrape the Empire site with no issue. If you are following this
path, and are on Windows, you will need to put the webdriver
in the root folder for that project and change the `chrome_driver_path = './chromedriver'`
to `chrome_driver_path = './chromedriver.exe'`. If you are on
Mac or Linux, just ensure you have the proper driver downloaded
and the existing path should work for you. For more on Selenium 
please [read the docs](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/).