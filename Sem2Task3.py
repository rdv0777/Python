"""Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в програм-
ме.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>"""

my_list = [None, 7.49, -77, 'Строка', 973, False]


def data_type(elem):
    for elem in range(len(my_list)):
        print(type(my_list[elem]))
    return


data_type(my_list)
