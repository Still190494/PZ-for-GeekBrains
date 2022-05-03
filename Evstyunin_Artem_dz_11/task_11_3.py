# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
#



class MyError(Exception):
    def __init__(self):
        pass

class myTypeError():
    def __init__(self):
        self.my_list = []
    def input_list(self):
        while True:
            try:
                try:
                    num_1 = int(input('Введите число:'))
                    self.my_list.append(num_1)
                    stop = input('Ведите "n" для остановки или "y" для продолжения ввода:')
                    if stop == "n":
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                error = input('Вы ввели не число! Хотите продолжить ?\n'
                              'Ведите "n" для остановки или "y" для продолжения ввода:')
                if error == 'n':
                    print(self.my_list)
                    break
                else:
                    self.input_list()
my_list = myTypeError()
my_list.input_list()





