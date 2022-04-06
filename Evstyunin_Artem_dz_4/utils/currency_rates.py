from decimal import *
import requests
def currency_rates(Currency):
    '''Функция показывающая курсы валют'''
    Currency = Currency.upper() # все, что вводится...приводится к верхнему регистру
    website = 'http://www.cbr.ru/scripts/XML_daily.asp'
    text = requests.get(website).text # данные с сайта
    idx = text.find('Date')
    date = text[idx + 6:idx + 16] # дата с сайта
    if Currency not in text:
        return None
    currency_rate = text[text.find('<Value>', text.find(Currency))+7:text.find('</Value>', text.find(Currency))] # курс валюты
    return f'{Decimal(currency_rate.replace(",","."))},{date}'
if __name__ == '__main__':
    import sys
    print(sys.argv)