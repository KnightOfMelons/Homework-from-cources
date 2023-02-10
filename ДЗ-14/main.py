# 3.
# Вам дана матричная сетка размера m x n,
# состоящая из положительных целых чисел.
#
# Выполняйте следующую операцию, пока сетка не станет пустой:
#
# Удалите элемент с наибольшим значением из каждой строки.
# Если существует несколько таких элементов, удалите любой из них.
# Добавьте к ответу максимальный из удаленных элементов.
# Обратите внимание, что количество столбцов уменьшается на
# один после каждой операции.
#
# Верните ответ после выполнения операций, описанных выше.
#
# Пример: [[1, 2, !4!], => [[1, !2!], => [[!1!], => [[],
#          [!3!, 3, 1]] =>  [!3!, 1]] =>  [!1!]] =>  []]
#             0 + 4   ||   4 + 3  ||  7 + 1 => Ответ: 8

print('\nЗадание 3\n') # Эту задачу я более-менее разобрал, было относительно легко. Но матрицы даются, конечно, тяжело

matrix = [[4,2,1],
          [1,3,3]]
print('Изначальные значения: ',matrix)

for i in matrix:
    i.sort(reverse = True)

sum = 0
for j in range(len(matrix[0])):
    answer = 0
    for h in range(len(matrix)):
        answer = max(answer, matrix[h].pop())
    sum += answer

print('\nОтвет: ',sum)

# 8.
# Вам дана целочисленная матричная сетка размера n x n.
#
# Создайте целочисленную матрицу max_local размера
# (n - 2) x (n - 2), такую, что:
#
# max_local[i][j] равно наибольшему значению матрицы
# 3 x 3 в сетке с центром вокруг строки i + 1 и столбца j + 1.
# Другими словами, мы хотим найти наибольшее значение
# в каждой непрерывной матрице 3 x 3 в сетке.
#
# Верните сгенерированную матрицу.

print('\nЗадание 8\n') # Это вообще тёмный лес. Я более-менее понял работу только благодаря тому, что
# использовал пайтон тренажер, который шаг за шагом показывал работу программы. Ненавижу матрицы.

def local_maxes(matrix):
    n = len(matrix)

    def local_max(matrix, row, col, radius):
        return  max(matrix[r][c]
                    for r in range(row - radius, row + radius + 1)
                    for c in range(col - radius, col + radius + 1))
    return  [[local_max(matrix, i, j, 1) for i in range(1, n - 1)]
             for j in range(1, n - 1)]

matrix = [[9, 9, 8, 1],
          [5, 6, 2, 6],
          [8, 2, 6, 4],
          [6, 2, 2, 2]]

print(local_maxes(matrix))