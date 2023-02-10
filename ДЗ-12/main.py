# Модуль 5. Файлы.
# Тема: Файлы. Часть 1

# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

print('Задание 1\n')

with open(file='1_task.txt', mode='r', encoding='UTF-8') as f:
    lines_1 = set(f.read().split())
    f.close()
    with open(file='1_task_second.txt', mode='r', encoding='UTF-8') as f:
        lines_2 = set(f.read().split())
        f.close()

print('Изначальные значения:\n\n', 'Первый файл: ', lines_1, '\n', 'Второй файл: ',lines_2, '\n')

print('Итог: ', lines_1.intersection(lines_2)) # intersection подсказал интернет

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

print('\nЗадание 2\n\n=== Работает только с Русскими буквами ===\n')

with open(file='2_task.txt', mode='r',encoding='UTF-8') as f:
    length = len(f.read()) # посмотрел длину всего файла
    line_count = sum(1 for line in open(file='2_task.txt', mode='r', encoding='UTF-8')) # посмотрел количество строк
    with open(file='2_task.txt', mode='r',encoding='UTF-8') as letters:
        result = list(letters.read().lower()) # создал новую переменную с нижним индексом, с которой буду работать
        result_with_letters = [i for i in result if i.isalpha() == True] # использую isalpha чтобы сохранить буквы
        count_vowels = 0 # количество гласных букв
        count_consonants = 0 # количество согласных букв
        for i in result_with_letters:
            if i in 'ауоыэяюёие': # проверяю на гласные
                count_vowels += 1
            else:
                count_consonants += 1 # а тут уже всё равно
        result_with_num = [i for i in result if i.isdigit() == True] # сохраняю в новую переменную только цифры
        f.close()
        letters.close()

print('Количество символов: ', length, '\nКоличество строк: ', line_count, '\nКоличество гласных букв: ', count_vowels,
      '\nКоличество согласных букв: ', count_consonants, '\nКоличество цифр: ', len(result_with_num))
# Сверху статистика и инфа ^ А снизу всё то же самое

# ОТ МЕНЯ:  А можно ли как-то снизу укоротить сие уродство? Типа чтобы в write() сразу несколько значений передать?
# а то он ругается на то, что мол один аргумент нужно передавать

with open(file='2_task_new.txt', mode='w',encoding='UTF-8') as result_file:
    result_file.write('Количество символов: ')
    result_file.write(str(length))
    result_file.write('\nКоличество строк: ')
    result_file.write(str(line_count))
    result_file.write('\nКоличество гласных букв: ')
    result_file.write(str(count_vowels))
    result_file.write('\nКоличество согласных букв: ')
    result_file.write(str(count_consonants))
    result_file.write('\nКоличество цифр: ')
    result_file.write(str(len(result_with_num)))

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

print('\nЗадание 3\n')

f_read = open(file='2_task.txt', mode='r', encoding='UTF-8')
f_write = open(file='3_task_new.txt', mode='w', encoding='UTF-8')

f_readlines = f_read.readlines()
f_readlines_1 = f_readlines[:-1]

for line in f_readlines_1:
    f_write.write(line)

print('Была убрана последняя строчка. Смотреть в файле - 3_task_new.txt. Изначально текст брался из 2_task.txt')

f_read.close()
f_write.close()

# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.

print('\nЗадание 4\n')

with open(file='2_task.txt', mode='r', encoding='UTF-8') as input_f:
    lines = input_f.readlines()

print('Самая длинная строка: ', max(lines, key=len), '\nЕё длинна: ', len(max(lines,key=len)))
input_f.close()

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово

print('\nЗадание 5\n')

import  re

with open(file='2_task.txt', mode='r', encoding='UTF-8') as f_5_task:
    find_word = f_5_task.read().lower()
    word_to_find_input = input('Введите слова для поиска: ')

    # ОТ МЕНЯ: это решение я подглядел в интернете, покажете эталонное решение? Хоть в файле отправьте

    print('Количество в тексе: ', len(re.findall(fr'\b{word_to_find_input}\b', find_word)))
    f_5_task.close()

# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

print('\nЗадание 6\n')

word_find_change = input('Какое слово вы хотите найти?: ')
word_change = input('На какое слово хотите заменить?: ')

with open(file='2_task.txt', mode='r', encoding='UTF-8') as word_in:
    text = word_in.read()
    text = text.replace(word_find_change, word_change)
    with open(file='6_task.txt', mode='w', encoding='UTF-8') as results:
        results.write(text)
        print('\nРезультат смотреть в файле 6_task.txt')
        word_in.close()
        results.close()

print('Это для Гита')