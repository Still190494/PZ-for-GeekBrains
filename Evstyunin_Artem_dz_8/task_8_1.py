# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?


import re
adress = re.compile(r'([A-z0-9]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email):
    my_list = adress.findall(email)
    if adress.match(email):
        username, domain = my_list[0]
        my_dict = {'username':username,'domain':domain}
    else:
        raise ValueError(f'wrong email: {email}')
    return my_dict

print(email_parse('Still190494@ya.ru'))