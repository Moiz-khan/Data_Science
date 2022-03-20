import requests
from bs4 import BeautifulSoup 

page = requests.get("https://www.goldenpages.uz/en/search/new/?active_lang=en&active_lang_link=%2Fen&region=0&Id=0&s=companies")


soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find('td', class_='Address')
print(a.text)
