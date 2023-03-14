"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
 str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int,
                 bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_total_income(self):
        return sum(self._income.values())


nam_surnam = Position("Петр", "Иванов", " Аналитик,", 150000, 50000)
print(f"{nam_surnam.get_full_name()},{nam_surnam.position}")
print(nam_surnam.get_total_income())
