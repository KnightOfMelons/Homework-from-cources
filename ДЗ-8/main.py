# Модуль 5. Функции.
# Тема: Функции. Часть 3

# Задание 1
# Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

print('Задание 1.\n')

def gcd(a, b) -> int:
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))
print('Наибольший общий делитель:', gcd(num_1, num_2))

# Задание 2
# Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа
# сообщает, сколько цифр числа угадано (быки) и сколько
# цифр угадано и стоит на нужном месте (коровы). После
# отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток. В программе
# необходимо использовать рекурсию.

print('\nЗадание 2.\n')

# ===== ОТ МЕНЯ ===== : Константин, вроде бы "Быки и коровы" - это то же самое, что и числовая угадайка? Я делал этот
# проект ещё с полгода назад, когда пытался сам изучить Python, посмотрите пожалуйста (хотелось бы просто мнение
# эксперта услышать ахахаха), а если что удалите задание - я переделаю по ТЗ, которое указано сверху

import random

def is_valid(num):
    return 0 < num < 100

# ===== ОТ МЕНЯ =====: ЕСЛИ ЧТО СРАЗУ ПОСЛЕ ВВЕДЕНИЯ ЦИФРЫ 1 ВЫДАЕТСЯ ПРАВИЛЬНЫЙ ОТВЕТ, ЧТОБЫ ВЫ ПОСМОТРЕЛИ КАК РАБОТАЕТ
# ПРОГРАММА

def working(answer):
    count = 0
    while count != 3:
        if is_valid(answer) == False:
            print('Неправильное введенное значение! Попробуй ещё раз.'.center(80))
            answer = int(input())
            continue
        if answer == num:
            print('\n============== Поздравляем, вы отгадали! Это было число:', num,'==================\n')
            print('============== Количество попыток:', count, '==================')
            break
        elif answer < num:
            print('Ответ меньше загадонного числа!'.center(80))
            count += 1
            answer = int(input())
            continue
        elif answer > num:
            print('Ответ больше загадонного числа!'.center(80))
            count += 1
            answer = int(input())
            continue
    if count == 3:
        print('Количество попыток израсходованно!\n'.center(80))


print('============================= Числовая угадайка =============================\n',
'Вам нужно отгадать сгенерированное компьютером числом в диапазоне от 1 до 100',
'Также будет даваться 3 попытки\n'.center(80),
'Чтобы начать игру нажмите 1 и Enter'.center(80), 'Чтобы выйти, нажмите 2 и Enter\n'.center(80),sep = '\n')

choise = int(input())

if choise == 1:
    num = random.randint(1, 100)
    print(num)
    print('Отгадайте загаданное число!'.center(80))
    answer = int(input())
    while True:
        if is_valid(answer) == False:
            print('Неправильное введенное значение! Попробуй ещё раз.'.center(80))
            answer = int(input())
            continue
        else:
            working(answer)
            break
elif choise == 2:
    print(quit)