import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = {
    "Top 250 Tv Series": "https://www.imdb.com/chart/toptv/"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

movie_names = []
yer = []
rating = []
content = []
genre = []

for name, url in urls.items():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    movie_data = soup.find_all('h3', class_='ipc-title__text')
    for store in movie_data:
        movie_name = store.text
        print(movie_name)
