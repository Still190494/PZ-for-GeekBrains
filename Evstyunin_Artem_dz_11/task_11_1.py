# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date):
        self.date = date
        print(date,type(date))

    @classmethod
    def int_data(cls, date):
        day, month, year = date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        print(f'{day:02} {month:02} {year}',type(day))

    @staticmethod
    def valid_date(date):
        day, month, year = date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)

        if 1 <= day <= 31 and 1 <= month <= 12 and 0 < year:
            return True
        else:
            raise ValueError('Введены не верные данные')




data_1 = Date('19-04-1994')

Date.int_data('19-04-1994')

print(Date.valid_date('09-04-1994'))
print(Date.valid_date('40-04-1994'))



