# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os
import sys

size = {}
def scanner(folder):
    if not os.path.exists(folder):
        return
    with os.scandir(folder) as files:
        for i in files:
            if os.path.isfile(i):
                bytes = 10 ** len(str(os.stat(i).st_size))
                size[bytes] = size.get(bytes, 0) + 1
            elif os.path.isdir(i):
                scanner(os.path.join(folder, i))
if __name__ == "__main__":
    if len(sys.argv) == 2:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()
    scanner(folder)
print(size)