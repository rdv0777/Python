# Задание 2.

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


tot_num = int(input("Введите время в секундах: "))
sec = tot_num % 60
just_min = (tot_num - sec) // 60
minutes = just_min % 60
hours = (just_min - minutes) // 60
print(f"Время в формате ч:м:с - {hours}:{minutes}:{sec}")
