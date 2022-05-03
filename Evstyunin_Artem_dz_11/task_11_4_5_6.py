# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


from abc import ABC,abstractmethod

class Office_equipment():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = int(quantity)
        self.printer = [name,price,quantity]
        self.scanner = [name,price,quantity]
        self.copier = [name,price,quantity]
        # self.printer = {'Наименование': self.name,
        #                 'Цена': self.price,
        #                 'Количество': self.quantity}
        # self.scanner = {'Наименование': self.name,
        #                 'Цена': self.price,
        #                 'Количество': self.quantity}
        # self.copier = {'Наименование': self.name,
        #                'Цена': self.price,
        #                'Количество': self.quantity}
        # self.printer = {self.name: (self.price, self.quantity)}
        # self.scanner = {self.name: (self.price, self.quantity)}
        # self.copier = {self.name: (self.price, self.quantity)}
    @abstractmethod
    def admission(self):
        pass


class Printer(Office_equipment):
    def admission(self):
        return self.printer
    def __add__(self, other):
        return f'{(self.printer[2] + other.printer[2])}'

class Skanner(Office_equipment):
    def admission(self):
        return self.scanner
    def __add__(self, other):
        return f'{(self.scanner[2] + other.scanner[2])}'

class Copier(Office_equipment):
    def admission(self):
        return self.copier
    def __add__(self, other):
        return f'{(self.copier[2] + other.copier[2])}'

class Storage(Office_equipment):
    pass


a = Printer('hp', 5000, 2)
b = Printer('canon', 5000, 1)
c = Printer('sony',6000,3)
print(c.admission())
print(a.admission() + b.admission() + c.admission())








