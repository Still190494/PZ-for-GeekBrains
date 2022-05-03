# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
#
class myZeroDivisionError(Exception):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def noZero(self):
        try:
            if self.num_2 == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            return 'На ноль делить нельзя'
        else:
            return (self.num_1 // self.num_2)

print(myZeroDivisionError(20,3).noZero())
print(myZeroDivisionError(20,0).noZero())





