"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет
на круглой грядке, причем кусты высажены только по окружности. Таким образом,
 у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
 Собирающий модуль за один заход, находясь непосредственно перед некоторым
 кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки."""

n = int(input("Введите колличество кустов: "))
a = [int(i) for i in input("Введите колличество ягод на каждом кусте через"
                           " пробел: ").split()]

maxsum = 0
if n != len(a):
    print("Введено не верное колличество кустов")
else:
    for i in range(n):
        cursum = sum(a[i:i + 3])
        if cursum > maxsum:
            maxsum = cursum
    if a[0]+a[-1]+a[-2]>maxsum:
        maxsum=a[0]+a[-1]+a[-2]
    if a[0]+a[-1]+a[1]>maxsum:
        maxsum=a[0]+a[-1]+a[1]
    print(maxsum)

print()