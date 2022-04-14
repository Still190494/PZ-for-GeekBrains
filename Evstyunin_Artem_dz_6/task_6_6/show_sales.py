# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

import sys

nums = sys.argv[1:]

with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) < 1:                        # если без условия
        for idx, line in enumerate(f,1):
            print(line.strip())
    f.seek(0)
    if len(nums) == 1:                       # если одно условие
        for idx, line in enumerate(f,1):
            if idx == int(nums[0]) and len(nums) == 1:
                print(line.strip())
    f.seek(0)
    if len(nums) > 1:                        # если два условия
        for idx, line in enumerate(f, 1):
            while idx <= int(nums[1]):
                if idx < int(nums[0]):
                    break
                elif idx == int(nums[0]):
                    print(line.strip())
                    break
                elif idx >= int(nums[0]):
                    print(line.strip())
                    break
