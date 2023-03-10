# Модуль 4. Строки. Списки.
# Часть 3

# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.

print('Задание 1\n')

import random
mass_1 = []
mass_2 = []
mass_3 = []

for i in range(10):
    mass_1.append(random.randint(0, 100))

for i in range(10):
    mass_2.append(random.randint(0, 100))

print('Все списки:', mass_2,mass_1, sep ='\n')
print()

mass_3 = mass_1 + mass_2
print('Список, содержащий элементы обоих списков:',mass_3)

mass_3 = list(set(mass_1 + mass_2))
print('Список, содержащий элементы обоих списков без повторений:',mass_3)

mass_3 = list(set(mass_1) & set(mass_2))
print('Список, содержащий элементы общие для двух списков:',mass_3)

mass_3 = list(set(mass_1) | set(mass_2))
print('Список, содержащий элементы уникальные элементы:',mass_3)

mass_3 =  [min(mass_1), max(mass_1), min(mass_2), max(mass_2)]
print('Список, содержащий только минимальное и максимальное значение каждого из списков:',mass_3)