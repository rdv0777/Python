"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass, height):
        self.mass = mass
        self.height = height
        asphalt_mass_1 = int(self._length * self._width * self.mass *
                             self.height)
        asphalt_mass_2 = asphalt_mass_1 / 1000
        print(f" {self._length}*{self._width}*{self.mass}*{self.height} = "
              f"{asphalt_mass_1} кг. = {asphalt_mass_2} т.")


roadbed = Road(5000, 20)
roadbed.asphalt_mass(25, 0.05)
