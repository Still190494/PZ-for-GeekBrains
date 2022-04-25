# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self,speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Машина поехала')
    def stop(self):
        print(f'Машина остановилась')
    def turn_left(self):
        print(f'Машина повернула налево')
    def turn_right(self):
        print(f'Машина повернула направо')
    def show_speed(self):
        print(f'{self.speed} км/ч - Текущая скорость автомобиля')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} км/ч - Превышение скорости')
        if self.speed < 60:
            print(f'{self.speed} км/ч - Текущая скорость автомобиля')
        # super().show_speed()
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} км/ч - Превышение скорости')
        if self.speed < 40:
            print(f'{self.speed} км/ч - Текущая скорость автомобиля')
        # super().show_speed()

class PoliceCar(Car):
    pass

towncar = TownCar(70,'Желтый','Городская машина',False)
sportcar = SportCar(250,'Красный','Спортивная машина',True)
workcar = WorkCar(50,'Желтый','Рабочая машина',False)
policecar = PoliceCar(110,'Желтый','Полицейская машина',True)

towncar.show_speed()
sportcar.show_speed()
workcar.show_speed()
policecar.show_speed()
towncar.go()
towncar.stop()
towncar.turn_right()
towncar.turn_left()
