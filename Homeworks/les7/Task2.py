"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
 которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
 параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @abstractmethod
    def cloth_value(self):
        pass

class Coat(Clothes):
    @property
    def cloth_value(self):
        return self.size / 6.5 + 0.5

class Suit(Clothes):
    @property
    def cloth_value(self):
        return 2 * self.height + 0.3

a = Coat('Galina', 48, 176)
b = Suit('Victor', 52, 191)

print(a.cloth_value)
print(b.cloth_value)

