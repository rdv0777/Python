"""Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы."""


def even_odd(n, even=0, odd=0):
    if n == 0:
        return even, odd

    current_n, last_digit = divmod(n, 10)

    if last_digit % 2 == 0:
        return even_odd(current_n, even + 1, odd)
    else:
        return even_odd(current_n, even, odd + 1)


n = int(input("Введите число: "))
even, odd = even_odd(n)
print(f"Количество четных и нечетных цифр в числе равно: ", even, odd)
