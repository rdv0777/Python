"""Задача 32: Определить индексы элементов массива (списка), значения которых
 принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
 больше заданного максимума)"""

list_el= [7, 10, 9, -7, 14, 9, 15, 21]

min_el = int(input("Введите минимальный элемент: "))
max_el = int(input("Введите максимальный элемент: "))

for i in range(len(list_el)):
    if min_el <= list_el[i] <= max_el:
        print(i)