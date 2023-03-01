# 6
# Создайте декоратор, который будет проверять
# возвращаемое функцией значение, и если оно меньше 0,
# будет заменять его на 0.
# Таким образом, этот декоратор будет
# 'отменять' отрицательные числа
import random

# @positive_numbers
# def sub(a,b):
#     return a - b

# print(sub(1,5)) => должно вернуть 0 благодаря декоратору

print('\nЗадание 6\n')

def positive_numbers(func):
    def doing(arg1, arg2):
        if arg1 - arg2 <= 0:
            return 0
        else:
            return arg1 - arg2
    return doing

@positive_numbers
def sub(a,b):
    return a - b

print(sub(1,5))

# 7
#
# Создавайте декоратор для повторной попытки
# выполнения функции с определенным количеством
# попыток в случае сбоя
#

print('\nЗадание 7\n') # Разбирали с вами на занятии.

import random

def retry(num):
    def decorator(func):
        def wrapper(*args):
            for i in range(num):
                try:
                    return func(*args)
                except Exception:
                    if i == num - 1:
                        raise Exception('Слишком много попыток вызова функции')
        return wrapper
    return decorator

@retry(num = 3)
def get_one():
    print('Вызов функции...')
    if random.randint(0,1):
        raise ValueError('Функция не сработала!')
    return 'Функция сработала успешно!'

print(get_one())