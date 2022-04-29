# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
# parameters size, height
from abc import ABC,abstractmethod


class Fabric_calculation(ABC):
    def __init__(self,parameters):
        self.parameters = parameters

    @abstractmethod
    def calculate(self):
        pass

class Coat(Fabric_calculation):
    @property
    def calculate(self):
        return f'Расход ткани на пальто - {self.parameters / 6.5 + 0.5:.2f}'

class Suit(Fabric_calculation):
    @property
    def calculate(self):
        return f'Расход ткани на костюм - {2 * self.parameters + 0.3:.2f}'



calculation = Coat(52)
calculation_1 = Suit(173)

print(calculation.calculate)
print(calculation_1.calculate)








