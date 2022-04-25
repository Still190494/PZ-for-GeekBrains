# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.



class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']
class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}({self.position})'
        print(full_name)
    def get_total_income(self):
        total_income = f'{self._income_wage + self._income_bonus}'
        print(total_income)
position = Position('Ксения','Новоселова','Главный специалист',{'wage': 50000, 'bonus': 6000})
position.get_full_name()
position.get_total_income()