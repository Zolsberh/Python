from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import csv
import re


def reprice(price: str) -> str:
    return re.sub(r'\xa0', '', price)


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_data(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, 'lxml')
    contain = soup.find('div', class_='row products-container')
    items = contain.find_all('div', class_='col-md-6')
    list_items = list()

    for item in items:
        try:
            name = item.find_next('a', class_='name').text.strip()
        except (ValueError, AttributeError):
            name = ''
        try:
            desc = item.find_next('div', class_='desc').text.strip()
        except (ValueError, AttributeError):
            desc = ''
        try:
            price_html = item.find_next('span', class_='price').text.strip()
            price = reprice(price_html)
        except (ValueError, AttributeError):
            price = ''
        try:
            players_html = item.find_next('i', class_='icon2-people').find_next('span').text
            players = f'_{players_html}'
        except (ValueError, AttributeError):
            players = ''
        try:
            time_html = item.find_next('i', class_='icon2-timer').find_next('span').text
            time = f'_{time_html}'
        except (ValueError, AttributeError):
            time = ''
        try:
            age = item.find_next('div', class_='age__number').text
        except (ValueError, AttributeError):
            age = ''
        try:
            link = item.find_next('a', class_='name')['href']
        except (ValueError, AttributeError):
            link = ''

        product = {'Название': name,
                   'Описание': desc,
                   'Цена': price,
                   'Количество игроков': players,
                   'Время игры': time,
                   'Возрастное ограничение': age,
                   'Ссылка': link
                   }
        list_items.append(product)
    return list_items


def writing_data(data: List[Dict[str, str]]) -> None:
    with open('products.csv', 'a', encoding='utf-8-sig') as file:
        fieldnames = list(data[0])
        writer = csv.DictWriter(file, fieldnames, delimiter=';', lineterminator='\r')
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def main():
    data = []
    for i in range(1, 104):
        url = f'https://hobbygames.ru/nastolnie?page={i}&parameter_type=0'
        data += get_data(get_html(url))
    writing_data(data)


if __name__ == '__main__':
    main()
