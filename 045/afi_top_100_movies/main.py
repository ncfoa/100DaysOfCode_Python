import gettext

from bs4 import BeautifulSoup
import requests

URL = "https://www.georgefox.edu/library/explore-contribute/collections/afi-top100-films.html"
data = requests.get(URL).text

s = BeautifulSoup(data, "html.parser")
entries = s.select(selector="td a")
movies = []
num = 1
for entry in entries:
    e = entry.text
    movies.append(f'{num}) {e}')
    num += 1

with open("movies.txt", "w") as f:
    for i in movies:
        f.write(i + "\n")