"""Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя."""


def rec(inp, num1, num2):
    while True:

        inp = input("Введите операцию (+, -, *, / или 0 для выхода): ")
        if inp == "0":
            break
        if inp == "+" or inp == "-" or inp == "*" or inp == "/":
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))

            if inp == "+":
                print("Ваш результат: ", num1 + num2)

            elif inp == "*":
                print("Ваш результат: ", num1 * num2)

            elif inp == "/":
                if num2 == 0:
                    print("На 0 дельть нельзя")
                    continue
                else:
                    print("Ваш результат: ", num1 / num2)
            elif inp == "-":
                print("Ваш результат: ", num1 - num2)

        else:
            print("Ошибка, введите (+, -, *, / или 0 для выхода)")
            continue


print(rec(1, 2, 3))