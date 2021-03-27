import requests

from bs4 import BeautifulSoup

data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

soup = BeautifulSoup(data.text,'html.parser')

movies_title = soup.select('#old_content > table > tbody > tr')

for title in movies_title:
    title_name = title.select_one('td.title > div > a')
    if title_name is not None:
        print(title_name.text)