mass = []

while True:
    choice_file = input('Введите название файла: ')

    if choice_file == 'quit':
        with open(file='new.txt', mode='w', encoding='UTF-8') as wr:
            wr.write(''.join(mass))
            break

    new_file = choice_file + '.txt'
    with open(file=new_file, mode='r', encoding='UTF-8') as f:
        mass.append(f.readline())
        print(mass)

    #     for i in mass:
    #         with open(file=i, mode='r', encoding='UTF-8') as f:
    #             result += f.read()
    #     with open(file='res.txt', mode='w', encoding='UTF-8') as j:
    #         j.write(result)
    #     break
    # else:
    #     mass.append(choice_file)

# with open(file='start.txt', mode='r', encoding='UTF-8') as f_1:
#     words_start = f_1.read()

# dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
#        'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh',
#        'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'I', 'й':'i', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
#        'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r',
#        'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'Kh', 'х':'kh',
#        'Ц':'Tc', 'ц':'tc', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y',
#        'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}
#
# with open(file='start.txt', mode='r', encoding='UTF-8') as f_1:
#     words_start = f_1.read()
#     words_start = list(words_start)
#     with open(file='results.txt', mode='w', encoding='UTF-8') as f_2:
#         for i in words_start:
#             f_2.write(f'{dic.get(i, i)}')


# with open(file='start.txt', mode='r', encoding='UTF-8') as f_1:
#     words_start = f_1.read().split()
# with open(file='ban_words.txt', mode='r', encoding='UTF-8') as f_2:
#     words_ban = f_2.read().split()
#
# with open(file='results.txt', mode='w', encoding='UTF-8') as f_3:
#     res = ''
#     for i in words_start:
#         if i.lower() not in words_ban:
#             res += f'{i} '
#     res = res[:-1]
#     f_3.write(res)


# letter = input('Введите одну букву: ')
# count = 0
#
# with open(file='test.txt', mode='r', encoding='UTF-8') as f:
#     for i in f.read().split():
#         if letter == i[0]:
#             count += 1
# print(count)

# with open(file='test.txt', mode='r', encoding='UTF-8') as f:
#     strings = f.readlines()
#     strings[-1] += '\n'
#     strings[0] = strings[0][:-1]
#     with open(file='second_file.txt', mode='w', encoding='UTF-8') as out:
#         for string in strings[::-1]:
#             out.write(string)

# with open(file= 'test.txt', mode='r',encoding='UTF-8') as first_fyle:
#     words = first_fyle.readline()
#     with open(file='second_file.txt', mode='w', encoding='UTF-8') as second_fyle:
#         while words != '':
#             second_fyle.write(words)
#             words = first_fyle.readline()

# with open(file='test.txt', mode='r', encoding='UTF-8') as f:
#     words = f.read().split()
#     print(words)
#     with open(file='new_file.txt', mode='w', encoding='UTF-8') as f_2:
#         f_2.write(' '.join([s for s in words if len(s) >= 7]))

# from gc import enable
#
# with open('test.txt', mode='r', encoding='UTF-8') as f:
#     print(len(f.read()))

# # Модуль 8. Кортежи, множества, словари
# # Тема: Кортежи, множества, словари. Часть 2
#
# # Задание 1
# # Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# # его рост. Требуется реализовать возможность добавления,
# # удаления, поиска, замены данных. Используйте словарь
# # для хранения информации.
#
# print('\nЗадание 1\n')
#
# dictionary = {
#     'Оскар Шмидт': 2.05,
#     'Сергей Белов': 1.9,
#     'Джерри Уэст': 1.91,
#     'Коби Брайант': 1.98,
#     'Оскар Робертсон': 1.96,
# }
#
# name_player = input('Какого баскетболиста добавить? ')
# height_player = int(input('Какой у него рост? '))
# dictionary[name_player] = height_player
#
# print('\n',dictionary,'\n')
#
# dictionary.pop(input('Какого баскетболиста хотите удалить? '))
# print('\n',dictionary,'\n')
#
# player_find = input('Какого игрока хотите найти? ')
# for i in (dictionary):
#     if i == player_find:
#         print('\nЕго рост:',dictionary[player_find], 'м.')
#
# player_find = input('\nКакого игрока хотите заменить? ')
# player_change = input('На какого игрока хотите заменить? ')
# player_change_height = int(input('Какой рост у нового игрока? '))
#
# dictionary[player_change] = dictionary.pop(player_find)
# dictionary[player_change] = player_change_height
#
# print('\n',dictionary,'\n')
#
# # Задание 4
# # Создайте программу «Книжная коллекция». Нужно
# # хранить информацию о книгах: автор, название книги,
# # жанр, год выпуска, количество страниц, издательство.
# # Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
# # хранения информации.
#
# print('\nЗадание 4\n')
#
# from pprint import pprint
# # ОТ МЕНЯ: нашел эту штуку в интернете для красивого вывода словаря чтобы не писать огромный for и тд
#
# dictionary_4_task = {
#     'Западный фронт': {
#         'Автор': 'Эрих Мария Ремарк',
#         'Название': 'На западном фронте без перемен',
#         'Жанр': 'Трагикомедия',
#         'Год выпуска': '1929',
#         'Издательство': 'Balster non Rolo'
#     },
#     'Python книга': {
#         'Автор': 'Анатолий Постолит',
#         'Название': 'Python и PyCharm',
#         'Жанр': 'Образовательная',
#         'Год выпуска': '2021',
#         'Издательство': 'bhv'
#     },
#     'Швейк': {
#         'Автор': 'Ярослав Гашек',
#         'Название': 'Похождение Швейка',
#         'Жанр': 'Военная комедия',
#         'Год выпуска': '1923',
#         'Издательство': 'Большие книги'
#     }
# }
#
# print('Изначальные значения:\n')
# pprint(dictionary_4_task)
#
# while True:
#     print('\n========== Нажмите ==========\n1 - чтобы добавить информацию\n2 - чтобы удалить элемент\n3 - поиск элемента'
#           '\n4 - для замены данных\n5 - для выхода из программы.')
#     choose_menu = int(input('\nВыберите дальнейшее действие: '))
#     if choose_menu == 1:
#         short_name_add = input('\nВведите короткое имя для обозначения: ')
#         author = input('\nВведите автора произведения: ')
#         name = input('\nВведите название произведения: ')
#         type_book = input('\nВведите жанр произведения: ')
#         year = input('\nВведите год выпуска: ')
#         published_by = input('\nКто издатель? ')
#
#         dictionary_4_task[short_name_add] = {'Автор': author,
#                                              'Название': name,
#                                              'Жанр': type_book,
#                                              'Год выпуска': year,
#                                              'Издательство': published_by
#                                              }
#         print('\n========== Новые значения: ==========\n')
#         pprint(dictionary_4_task)
#     elif choose_menu == 2:
#         dictionary_4_task.pop(input('\nКакой элемент вы хотите удалить? Просто скопируйте название: '))
#         print('\n========== Новые значения: ==========\n')
#         pprint(dictionary_4_task)
#     elif choose_menu == 3:
#         book_find = input('\nКакую книгу хотите найти? ')
#         for i in (dictionary_4_task):
#             if i == book_find:
#                 print('\n========== Ваша книга: ==========\n')
#                 pprint(dictionary_4_task[book_find])
#     elif choose_menu == 4:
#         book_find = input('\nКакой элемент вы хотите изменить? Просто скопируйте краткое название: ')
#         print()
#         pprint(dictionary_4_task[book_find])
#         change = input('\nЧто вы хотите тут изменить? ')
#         if change == 'Автор':
#             change_inside = input('\nНа какого автора хотите заменить? ')
#             dictionary_4_task[book_find]['Автор'] = change_inside
#             print('\n========== Новые значения: ==========\n')
#             pprint(dictionary_4_task[book_find])
#         elif change == 'Название':
#             change_inside = input('\nКакое новое название вы хотите присвоить? ')
#             dictionary_4_task[book_find]['Название'] = change_inside
#             print('\n========== Новые значения: ==========\n')
#             pprint(dictionary_4_task[book_find])
#         elif change == 'Жанр':
#             change_inside = input('\nКакой новый жанр вы хотите присвоить? ')
#             dictionary_4_task[book_find]['Жанр'] = change_inside
#             print('\n========== Новые значения: ==========\n')
#             pprint(dictionary_4_task[book_find])
#         elif change == 'Год выпуска':
#             change_inside = input('\nКакой год выпуска вы хотите присвоить? ')
#             dictionary_4_task[book_find]['Год выпуска'] = change_inside
#             print('\n========== Новые значения: ==========\n')
#             pprint(dictionary_4_task[book_find])
#         elif change == 'Издательство':
#             change_inside = input('\nНа какое издательство вы хотите поменять? ')
#             dictionary_4_task[book_find]['Издательство'] = change_inside
#             print('\n========== Новые значения: ==========\n')
#             pprint(dictionary_4_task[book_find])
#         else:
#             print('\nБыли введены неправильные значения')
#     elif choose_menu == 5:
#         print('\n========== Программа завершается ==========')
#         break
#     else:
#         print('\nБыли введены неправильные значения! Попробуйте ещё.')