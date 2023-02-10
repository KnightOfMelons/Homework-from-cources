# Модуль 5. Функции.
# Тема: Функции. Часть 1

# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

print('Часть 1. Задание 1.\n')

def text():
    return print("Don't compare yourself with anyone in this world… \nif you do so, "
                 "you are insulting yourself.  \n                                               Bill Gates")

text()

# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

print('\nЗадание 2.\n')

num_1 = int(input('Введите 1 число: '))
num_2 = int(input('Введите 2 число: '))
list = []

def even_numbers(num_1,num_2):
    for i in range(num_1,num_2):
        if i % 2 == 0:
            list.append(i)
    print(*list)

even_numbers(num_1,num_2)

# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

print('\nЗадание 3.\n')

def squares(number_of_stars,symbol,bulevo):
    r = symbol * number_of_stars
    if not bulevo:
        m = symbol + " " * (number_of_stars- 2) + symbol
    else:
        m = r
    print(r)
    for i in range(number_of_stars - 2):
        print(m)
    print(r)

number_of_stars = int(input('\nВведите длину стороны квадрата: '))
symbol = input('Введите символ для заполнения квадрата: ')
flag = input('Хотите сделать квадрат пустой или заполненный? Да или нет: ').lower()

if flag == 'да' or flag == 'yes':
    print()
    squares(number_of_stars, symbol, True)
elif flag == 'нет' or flag == 'no':
    print()
    squares(number_of_stars, symbol, False)
else:
    print('Введены некорректные значения!')

# Задание 4
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

print('\nЗадание 4.\n')

number_1,number_2,number_3,number_4,number_5 = (int(input('Введите число: ')) for _ in range(5))

def minimum_num(number_1,number_2,number_3,number_4,number_5):
    list = []
    list.append(number_1)
    list.append(number_2)
    list.append(number_3)
    list.append(number_4)
    list.append(number_5)
    print('\n',min(list))

minimum_num(number_1,number_2,number_3,number_4,number_5)

# Задание 5
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

print('\nЗадание 5.\n')

num_1 = int(input('Введите 1 границу диапазона: '))
num_2 = int(input('Введите 2 границу диапазона: '))


def range_mult(num_1,num_2):
    multiplication = 1

    if num_2 > num_1:
        for i in range(num_1, num_2+1):
            multiplication *= i
    elif num_1 > num_2:
        for i in range(num_2, num_1+1):
            multiplication *= i


    print('\nПроизведение чисел в диапазоне равно: ', multiplication)

range_mult(num_1,num_2)

# Задание 6
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

print('\nЗадание 6.\n')

number = int(input('Напишите число, количество цифр в котором вы хотите посчитать: '))

def count_numbers(number):
    answer = len(str(number))
    print('Количество цифр в числе: ', answer)

count_numbers(number)

# Задание 7
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.

print('\nЗадание 7.\n')

num = input('Введите число для проверки на палиндромность: ')

def palindrom(num):
    if num == num[::-1]:
        # ОТ МЕНЯ: я так и не понял, тут булево значение должно быть или тупо текст true или false должен быть?
        print('\nTrue')
    else:
        print('\nFalse')

palindrom(num)