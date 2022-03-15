# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
n = input('Введите число прописью от 0 до 10')
def num_translate(n):
    if n == 'zero':
        print ('ноль')
        exit()
    if n == 'one':
        print ('один')
        exit()
    if n == 'two':
        print ('два')
        exit()
    if n == 'three':
        print ('три')
        exit()
    if n == 'four':
        print ('четыре')
        exit()
    if n == 'five':
        print ('пять')
        exit()
    if n == 'six':
        print ('шесть')
        exit()
    if n == 'seven':
        print ('семь')
        exit()
    if n == 'eight':
        print ('восемь')
        exit()
    if n == 'nine':
        print ('девять')
        exit()
    if n == 'ten':
        print ('десять')
        exit()
    else:
        print(None)
num_translate(n)
