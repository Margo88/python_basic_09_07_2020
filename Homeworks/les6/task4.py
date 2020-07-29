"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы:
go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина поворачивает {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Hyundai Solaris', False)

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    def __init__(self, name):
        super().__init__(140, 'White&Blue', name, True)

priora = SportCar(109, 'Мокрый асфальт', 'Lada Priora')
print(priora.is_police)

zhiguli = TownCar(80, 'Баклажан', 'Lada sedan')
zhiguli.show_speed()

ahmed = WorkCar(176, 'Желтый')
ahmed.turn('из второго ряда')

acab = PoliceCar('BMW X5M')
acab.go()
acab.show_speed()
acab.stop()
