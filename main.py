# 1. Создайте массив из 10 элементов со случайными числами от 0 до 99. Найдите максимальное и минимальное значение этого массива.

import random

arr = [random.randint(0, 99) for i in range(10)]

print(max(arr), min(arr))

min_el = arr[0]
max_el = arr[0]

for el in arr:
    if min_el > el:
        min_el = el
    if max_el < el:
        max_el = el

print(max_el, min_el)

# 2. Создайте массив из 10 строк с фамилиями пользователей: Иванов, Петров, Сидоров, Алексеева, Казанцев, Антропов, Анисимова, Кузнецов, Соловьев, Кошкина.
# Выведите список пользователей в алфавитном порядке.

string_arr = ["Иванов", "Петров", "Сидоров", "Алексеева", "Казанцев", "Антропов", "Анисимова", "Кузнецов", "Соловьев", "Кошкина"]

print(sorted(string_arr))

for i in range(len(string_arr) - 1):
    for j in range(len(string_arr) - i - 1):
        if string_arr[j] > string_arr[j + 1]:
            string_arr[j], string_arr[j + 1] = string_arr[j + 1], string_arr[j]

print(string_arr)

# 3. Создайте программу, которая выводит интервал дней текущей недели: '07.10.2019-13.10.2019'.

from datetime import date, datetime, timedelta

today = date.today()
start = today - timedelta(days=today.weekday())
end = start + timedelta(days=6)
print(start.strftime('%d.%m.%Y') + "-" + end.strftime('%d.%m.%Y'))

# 4. Дан массив ['cat', 'dog', 'tiger']. Необходимо изменить его так, чтобы все элементы были написаны с заглавной буквы.

animals = ['cat', 'dog', 'tiger']

for i in range(len(animals)):
    animals[i] = animals[i].capitalize()

print(animals)

# 5. Строку 'Hello world!' преобразуйте в массив ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d", "!"].

common_str = 'Hello world!'
print(list(common_str))

# 6. Создайте массив с названиями месяцев на русском языке. Извлеките месяцы с самым коротким и с самым длинным названием.

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

print(min(months, key=len))
print(max(months, key=len))

# 7. Создайте словарь, в котором в качестве ключа выступает название планеты Солнечной системы, а в качестве значения — масса планеты. 
# Сформируйте две коллекции с тремя самыми легкими и тремя самыми тяжелыми планетами. Выведите их в стандартный поток вывода.

from collections import OrderedDict
from operator import itemgetter 

planet = {"Mercury": 3.301e23, "Venus": 4.867e24, "Earth": 5.972e24, "Mars": 6.417e23, "Jupiter": 1.899e27, "Saturn": 5.685e26, "Uranus": 8.682e25, "Neptune": 1.024e26}
ordered_planet = OrderedDict(sorted(planet.items(), key = itemgetter(1)))

print(list(ordered_planet.items())[:3])
print(list(ordered_planet.items())[-3:])
