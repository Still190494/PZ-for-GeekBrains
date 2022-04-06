# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
my_list = [10.66, 74.04, 23.65, 38.87, 7.3, 98, 68.43, 9.99, 84.66, 7.4]
print (id(my_list))
my_list.sort()
print (id(my_list))

for price in my_list:
    rub = int(price) # рубли
    k = (round((price - rub),2)) * 100 # копейки float
    kk = int(k) # копейки
    print (f'{rub} руб. {kk:02} коп.', end=' ,')

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

new_list = (sorted(my_list, reverse=True))
for price in new_list[4::-1]:
    rub = int(price)  # рубли
    k = (round((price - rub),2)) * 100 # копейки float
    kk = int(k) # копейки
    print (f'{rub} руб. {kk:02} коп.', end=' ,')
