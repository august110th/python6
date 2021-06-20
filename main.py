import requests
from bs4 import BeautifulSoup

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('ошибка запроса')

text = response.text
soup = BeautifulSoup(text, features='html.parser')
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

articles = soup.find_all('article')

for i in articles:
    title = {i.find('a', class_='post__title_link').text}
    data = i.find('span',class_="post__time" ).text
    link = i.find('a', class_='post__title_link', href = True)
    if KEYWORDS & title:
        print(title)
        print(data)
        print(link['href'])
