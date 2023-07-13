# python3 -m venv venv - создание виртуального окружения 
# soruce ./venv/bin/activate - активация виртуального окружения
# pip freeze - показывает список установленных библиотек
# deactivate - выйти из виртуального

# pip install requests
# lxml
# beautifulsoup4
import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')


    catalog = soup.find('div', class_='catalog-list')
    cars = catalog.find_all('a', class_='catalog-list-item')
    
    
    for i in cars:
        try:
            title = i.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = ''
        try:
            img = i.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img = ''

        with open('cars.csv', 'a') as file:
            fields = ['title', 'image']
            writer = csv.DictWriter(file, delimiter=',', fieldnames=fields)
            writer.writerow({'title': title, 'image': img})

def main():
    URL = 'https://cars.kg/offers/'
    html = get_html(URL)
    get_data(html)




main()
