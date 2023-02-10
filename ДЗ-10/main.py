# Модуль 8. Кортежи, множества, словари
# Тема: Кортежи, множества, словари. Часть 1

# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах

print('\nЗадание 1\n')

first_tuple = (1,2,3,4,5,6,7,8,9,10)
second_tuple = (1,3,6,9,12)
third_tuple = (1,2,5,6,9,10)

print(tuple(set(first_tuple) & set(second_tuple) & set(third_tuple)))

# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.

print('\nЗадание 2\n')

first_tuple = (1,2,2,2,3,3,3,4,5,6,7,8,9,10)
second_tuple = (1,3,6,6,6,9,12,12)
third_tuple = (1,1,2,5,6,9,10,12,10,12)

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers(first_tuple))
print(get_unique_numbers(second_tuple))
print(get_unique_numbers(third_tuple))

# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

print('\nЗадание 3\n')

# ОТ МЕНЯ: с этим заданиям возникли трудности, мозг вообще отказывался понимать как это всё делать
# Нашел решение в интренете, но тут при выводе указывает только True или False на числе, которое проходит по условию
# Пришлите как-нибудь эталонное решение, пожалуйста

def find_match(*args):
    return tuple(len(set(arg)) == 1 for arg in zip(*args))


first_tuple = (1, 2, 3, 4, 5)
second_tuple = (1, 2, 3, 4, 5)
third_tuple = (1, 6, 3, 4, 5)

print(find_match(first_tuple, second_tuple, third_tuple))
