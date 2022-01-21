from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
from decimal import Decimal
import sys


def currency_rates(cur):
    """output to the console currency rate on the current date"""
    currency = {}
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.text, 'lxml')
    charcodes = soup.find_all('charcode')
    values = soup.find_all('value')
    date = datetime.date(datetime.strptime(soup.valcurs['date'], "%d.%m.%Y"))
    for i in range(len(charcodes)):
        currency[str(charcodes[i].text)] = (Decimal(values[i].text.replace(',', '.')).quantize(Decimal("1.00")))
    if cur.upper() not in currency.keys():
        return print('Валюты с таким идентификатором нет')
    else:
        return print(f'На {date} курс {cur.upper()} равен {currency.get(cur.upper())} руб.')


if __name__ == '__main__':
    exit(currency_rates(sys.argv[0]))
