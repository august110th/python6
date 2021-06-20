import requests
from bs4 import BeautifulSoup

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('ошибка запроса')

text = response.text
soup = BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
