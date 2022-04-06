# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str,
# решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
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


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('XXX'))













# idx = response.text.find('Date')
# # date = response.text[idx+6:idx+16]
