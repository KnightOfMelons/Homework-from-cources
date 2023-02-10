# Модуль 3. Циклы.
# Часть 5

# Задание
# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.

while True:
    choise = input('\nВведите номер фигуры, вам выдастся соответствующий результат (а,б,в,г,д,е,ж,з,и,к).'
                   'Напишите Ы для выхода: ').lower()

    print()

    if choise == 'а':
        for i in range(5, 0, -1):
            print((8 - i) * ' ' + i * '*')
    elif choise == 'б':
        for j in range(5):
            print(j * '*')
    elif choise == 'в':
        for i in range(0, 11):
            print(' ' * i + '*' * (11 - i * 2) + ' ' * i)
    elif choise == 'г':
        a = 7
        m = (2 * a) - 2
        for i in range(0, a):
            for j in range(0, m):
                print(end=" ")
            m = m - 1
            for j in range(0, i + 1):
                print("*", end=' ')
            print(" ")
    elif choise == 'д':
        # ОТ СЕБЯ: Если что я это решение списал, так как моя голова просто не понимала как сделать песочные часы,
        # но решение разобрал, более-менее понятно
        print(*[('* ' * i + '*').rjust(7 * 2 + i) for i in range(6, 0, -1)],
              *[('* ' * i + '*').rjust(7 * 2 + i) for i in range(7)], sep='\n')
    elif choise == 'е':
        for i in range(1, 6):
            print("*" * i, end="")
            print(" " * (6 - i) * 2, end="")
            print("*" * i)
        for i in range(6, 0, -1):
            print("*" * i, end="")
            print(" " * (6 - i) * 2, end="")
            print("*" * i)
    elif choise == 'ж':
        for i in range(5):
            for j in range(i):
                print("*", end=" ")
            print('*')
        for i in range(5 - 2, -1, -1):
            for j in range(i):
                print("*", end=" ")
            print('*')

    # ОТ СЕБЯ: это я тоже нашел в интернете, но это решение мне непонятно, можете прислать эталонное?
    elif choise == 'з':
        rows = 5
        i = 1
        while i <= rows:
            j = i
            while j < rows:
                # display space
                print(' ', end=' ')
                j += 1
            k = 1
            while k <= i:
                print('*', end=' ')
                k += 1
            print()
            i += 1

        i = rows
        while i >= 1:
            j = i
            while j <= rows:
                print(' ', end=' ')
                j += 1
            k = 1
            while k < i:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1

    elif choise == 'и':
        print("\n".join("* " * i for i in range(7, 0, -1)))
    elif choise == 'к':
        rows = 6
        for row in range(1, rows):
            for j in range(rows, 0, -1):
                if j > row:
                    print(" ", end=' ')
                else:
                    print('*', end=' ')
            print("")
    elif choise == 'ы':
        print('\nПрограмма закрылась, ВСЕГО ХО-РО-ШЕ-ГО')
        break
    else:
        print('\nВведены неверные значения! Пробуйте заново.\n')