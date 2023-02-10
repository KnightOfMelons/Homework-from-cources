# Модуль 2. Операторы ветвлений
# ===== Часть 2 ======

# Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник,
# 2 — вторник и т.д.

print('Часть 2. Задание 1.\n')
choose = int(input('Введите число дня недели: '))
if choose == 1:
    print('День недели - понедельник')
elif choose == 2:
    print('День недели - вторник')
elif choose == 3:
    print('День недели - среда')
elif choose == 4:
    print('День недели - четверг')
elif choose == 5:
    print('День недели - пятница')
elif choose == 6:
    print('День недели - суббота')
elif choose == 7:
    print('День недели - воскресенье')
else:
    print('Введены неверные значения!')

# Задание 2.
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

print('\nЗадание 2.\n')
choose_month = int(input('Введите число месяца: '))
if choose_month == 1:
    print('Ваш месяц - Январь')
elif choose_month == 2:
    print('Ваш месяц - Февраль')
elif choose_month == 3:
    print('Ваш месяц - Март')
elif choose_month == 4:
    print('Ваш месяц - Апрель')
elif choose_month == 5:
    print('Ваш месяц - Май')
elif choose_month == 6:
    print('Ваш месяц - Июнь')
elif choose_month == 7:
    print('Ваш месяц - Июль')
elif choose_month == 8:
    print('Ваш месяц - Август')
elif choose_month == 9:
    print('Ваш месяц - Сентябрь')
elif choose_month == 10:
    print('Ваш месяц - Октябрь')
elif choose_month == 11:
    print('Ваш месяц - Ноябрь')
elif choose_month == 12:
    print('Ваш месяц - Декабрь')
else:
    print('Введены неправильные значения!')

# Задание 3.
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

print('\nЗадание 3.\n')
number_third = int(input('Введите число и мы скажем, больше ли оно нуля, меньше или равно: '))
if number_third == 0:
    print('Number is equal to zero')
elif number_third > 0:
    print('Number is positive')
elif number_third < 0:
    print('Number is negative')
else:
    print('Введены неверные значения!')

# Задание 4.
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.

print('\nЗадание 4.\n')
number_1, number_2 = (int(input('Введите число: ')) for _ in range(2))
if number_1 == number_2:
    print('Числа равны.')
elif number_1 > number_2:
    print('Число 1 больше числа 2: ', number_2, number_1)
elif number_1 < number_2:
    print('Число 2 больше числа 1: ', number_1, number_2)
else:
    print('Введены неверные значения!')

# ===== Часть 3 ======
# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.

print('\nЧасть 3. Задание 1.\n')
num_third_part = int(input('Введите число в диапазоне от 1 до 100: '))

if (num_third_part >= 1 and num_third_part <= 100) and num_third_part % 3 == 0:
    print('Fizz')
elif (num_third_part >= 1 and num_third_part <= 100) and num_third_part % 5 == 0:
    print('Buzz')
elif (num_third_part >= 1 and num_third_part <= 100) and num_third_part % 3 == 0 and num_third_part % 5 == 0:
    print('Fizz Buzz')
elif (num_third_part >= 1 and num_third_part <= 100) and num_third_part % 3 != 0 and num_third_part % 5 != 0:
    print('Ваше число: ', num_third_part)
elif not(num_third_part >= 1 and num_third_part <= 100):
    print('Введены неверные значения!')

# Задание 2.
# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.
print('\nЗадание 2.\n')

# ===== ОТ МЕНЯ =====
# Я не совсем понял как тут нужно было реализовать программу, поэтому сделал так, чтобы пользователь ввел 2 значения,
# первое - само число, а второе - число возведения степени с соответствующей проверкой от 0 до 7 включительно.
num_degree = int(input('Введите число для возведение числа в степень: '))
num_extent = int(input('Введите степень: '))

if num_extent >= 0 and num_extent <= 7:
    print('Результат: ', num_degree ** num_extent)
else:
    print('Введены неверные значения!')

# Задание 3.
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.

print('\nЗадание 3.\n')

# Тут тоже я не понял что конкретно нужно сделать, но немного усовершенствовал программу.
# Пользователь вводит то количество операторов, которое он хочет сделать, затем проставляет прейскурант вручную,
# а потом программа выводит все значения в удобном для чтения виде

mass_operators = []
operators = int(input('Сколько операторов вы хотите сделать?: '))

for _ in range (operators):
    mass_operators.append(int(input('Введите стоимость услуг оператора (в руб.): ')))

count = 0
count_opeartors = 1

for i in mass_operators:
    print('Оператор',count_opeartors, 'стоимость: ', mass_operators[count], end='\n')
    count += 1
    count_opeartors += 1

# Задание 4.
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

print('\nЗадание 4.\n')

answer_1 = 0
answer_2 = 0
answer_3 = 0

level_sells_1 = int(input('Введите уровень продаж 1 менеджера: '))
level_sells_2 = int(input('Введите уровень продаж 2 менеджера: '))
level_sells_3 = int(input('Введите уровень продаж 3 менеджера: '))

if level_sells_1 <= 500:
    answer_1 = (level_sells_1 / 100) * 3
elif level_sells_1 > 500 and level_sells_1 <= 1000:
    answer_1 = (level_sells_1 / 100) * 5
elif level_sells_1 > 1000:
    answer_1 = (level_sells_1 / 100) * 8

if level_sells_2 <= 500:
    answer_2 = (level_sells_2 / 100) * 3
elif level_sells_2 > 500 and level_sells_2 <= 1000:
    answer_2 = (level_sells_2 / 100) * 5
elif level_sells_2 > 1000:
    answer_2 = (level_sells_2 / 100) * 8

if level_sells_3 <= 500:
    answer_3 = (level_sells_3 / 100) * 3
elif level_sells_3 > 500 and level_sells_3 <= 1000:
    answer_3 = (level_sells_3 / 100) * 5
elif level_sells_3 > 1000:
    answer_3 = (level_sells_3 / 100) * 8

if answer_1 > answer_2 > answer_3 or answer_1 > answer_3 > answer_2:
    print('Первый менеджер получил лучший результат и зарплату: ', answer_1 + 200, '$')
elif answer_2 > answer_1 > answer_3 or answer_2 > answer_3 > answer_1:
    print('Второй менеджер получил лучший результат и зарплату: ', answer_2 + 200, '$')
elif answer_3 > answer_2 > answer_1 or answer_3 > answer_1 > answer_2:
    print('Третий менеджер получил лучший результат и зарплату: ', answer_3 + 200, '$')
else:
    print('В условиях задачи такого не было. Значит никто зарплату не получит.')
