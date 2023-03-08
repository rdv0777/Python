"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import random

n = round(random() * 100)


def guess_num(n, count=0):
    m = int(input("Введите число: "))
    count += 1
    if count == 10:
        print("Вы не отгадали, загаданное число:")
        return n
    elif m > n:
        print("Введённое число больше загаданного.")
        return guess_num(n, count)
    elif m < n:
        print("Введённое число меньше загаданного.")
        return guess_num(n, count)
    else:
        print("Вы отгадали загаданное число: ")
        return n


result = guess_num(n)
print(result)