# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

import csv
import json
import itertools
users = open('users.csv', 'r', encoding='utf-8')
hobby = open('hobby.csv', 'r', encoding='utf-8')
list_users = list(users)
list_hobby = list(hobby)
if len(list_users) < len(list_hobby):
    exit(1)
users.seek(0)
hobby.seek(0)
dic = ((fio.strip(),hob.strip()) for fio,hob in itertools.zip_longest(users,hobby) if hob is not None)
dict1 = dict(dic)
print(dict1)
file = open('dict.json', 'w', encoding='utf-8')
json.dump(dict1, file, ensure_ascii=False)
file.close()









