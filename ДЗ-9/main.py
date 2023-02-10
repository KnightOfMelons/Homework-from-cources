dictionary = {
    'Молдавия': 'Кишинев',
    'Россия': 'Париж',
    'ЮАР': 'КНР'
}

country = input('Какую страну добавить? ')
city = input('Какой город добавить? ')
dictionary[country] = city

print(dictionary)

dictionary.pop(input('Какую страну хотите удалить? '))
print(dictionary)

country_find = input('Какую страну вам найти? ')
for i in (dictionary):
    if i == country_find:
        print(dictionary[country_find])

country_change = input('Страна для замены: ')
city_change = input('Город для замены: ')
dictionary[country_change] = dictionary[city_change]
print(dictionary)

dictionary = {
    'name': 'Кенни',
    'age': 25,
    'salary': 8000,
    'city': 'New York'
}

dictionary_second = {}
dictionary_second = dictionary.copy()
dictionary_second.pop('age')
dictionary_second.pop('city')

dictionary.pop('name')
dictionary.pop('salary')

print(dictionary)
print(dictionary_second)

first_dict = {}

for i in range(1,5):
    first_dict[i] = input('Введите элемент: ')
print(first_dict, end = '\n')

first_dict.pop(int(input('\nКакой элемент хотите удалить? ')))

print('\n',first_dict)

x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
print({**x,**y})

from random import randint

s = tuple(randint(0, 999) for i in range(10))
print(s)

one_number, two_number, three_number = 0, 0, 0

for i in s:
    if i < 10:
        one_number += 1
    elif i < 100:
        two_number += 1
    elif i < 1000:
        three_number += 1

print(f'Одна цифра: {one_number}, две цифры: {two_number}, три цирфы: {three_number}')

# Модуль 7. Сортировка и поиск.
# Тема: Сортировка и поиск. Часть 1

# Задание 1
# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

print('\nЗадание 1\n')

mass_first = [1,23,12,35,69,12,45,10,20,145,5]
sum_1 = 0

print('Изначальное значение списка:', mass_first)

for i in mass_first:
    sum_1 += i

if sum_1 / len(mass_first) > 0:
    calculations = int(len(mass_first) * 0.66)
    mass_1 = mass_first[:calculations]
    mass_1.sort()

    mass_2 = mass_first[calculations:]
    mass_2.sort( reverse = True)

    print('\nПервый вариант. Конечное значение:',mass_1 + mass_2)

print('\n==================================================================')

mass_second = [1,-20,-30,-100,10,20,10,-10,0,-10,-658]
sum_2 = 0

print('\nИзначальное значение списка:', mass_second)

for j in mass_second:
    sum_2 += j

if sum_2 / len(mass_second) < 0:
    calculations = int(len(mass_second) * 0.33)
    mass_1 = mass_second[:calculations]
    mass_1.sort()

    mass_2 = mass_second[calculations:]
    mass_2.sort(reverse= True)

    print('\nВторой вариант. Конечное значение:', mass_1 + mass_2)
# Задание 2
# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если
# средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.

print('\nЗадание 2\n')

mass = []
choose = 0
summ = 0

for i in range(10):
    num = int(input('Введите число от 1 до 12: '))
    if num <= 0 or num > 12:
        print('\nБыли введены некорректные значение!')
        break
    else:
        mass.append(num)
        summ += num

print(mass)

while True:
    print('\nЧто вы хотите выбрать?\n1 - Вывод всех оценок\n2 - Пересдача экзамена\n3 - Выходит ли стипендия?\n'
          '4 - Вывод отсортированного списка оценок\n5 - Выход')
    choose = int(input('\nВаш выбор?\n\n'))
    if choose == 0 or choose > 5:
        print('Введены неверные значения!')
        continue
    elif choose == 1:
        print('\nВаши оценки:', *mass)
    elif choose == 2:
        print('\nОценки: ', *mass, '\n\nКакую оценку желаете заменить?: \n')
        choose_number = int(input('Номер оценки: '))
        choose_number_answer = int(input('На какую оценку заменить?: '))
        mass[choose_number] = choose_number_answer
        print('\nОценки:', *mass)
    elif choose == 3:
        if summ/10 > 10.7:
            print('\nВам положена стипендия. Ваш средний балл:', summ/10)
        else:
            print('\nВам не положена стипендия. Ваш средний балл:', summ/10,'Нужно больше 10.7')
    elif choose == 4:
        if int(input('\nВыберите тип сортировки. 1 - по возрастанию. 2 - по убыванию: ')) == 1:
            mass.sort()
            print('\nСписок оценок по возрастанию: ', mass)
        elif int(input('\nВыберите тип сортировки. 1 - по возрастанию. 2 - по убыванию: ')) == 2:
            mass.sort(reverse=True)
            print('\nСписок оценок по убыванию: ', mass)
        else:
            print('\nВведены некорректные значения')
    elif choose == 5:
        print('\n===== Программа завершается =====')
        break

# Задание 3
# Написать программу, реализующую сортировку списка
# методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку
# нет смысла — список отсортирован.

print('\nЗадание 3\n')

from random import randint

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

mass_nums = [randint(1, 100) for x in range(1, 10)]
print('Список до: ', mass_nums, '\n')
bubble_sort(mass_nums)
print('Список после: ', mass_nums)