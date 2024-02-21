import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/120.0.0.0 Safari/537.3'}


response = requests.get(url, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', {'class': 'product_pod'})

    for i in books:
        title = i.h3.a["title"]

        price = i.find("p", {"class": "price_color"}).text

        availability = i.find('p', {'class': 'instock availability'}).text.strip()

        image = i.img['src']

        print('\nНазвание книги:', title)
        print('Цена:', price)
        print('Наличие на складе:', availability)
        print('Ссылка на фото:', image)
        print('*****************')

elif response.status_code == 403:
    print('Доступ запрещен к этому сайту!!!')

else:
    print(f'Ошибка вот ваша ошибка {response.status_code}')