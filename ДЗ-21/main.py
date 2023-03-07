# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Перегрузка операторов. Часть 5

# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

print('\nЗадание 1\n')

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
        self.length = self.radius * 3.14 * 2

    # # ■ Проверка на равенство радиусов двух окружностей
    # # (операция = =);

    def __eq__(self, other):
        return Circle(self.radius == other.radius)

    # # ■ Сравнения длин двух окружностей (операции >, <,
    # # <=,>=);

    def __gt__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __ge__(self, other):
        return self.length >= other.length

    # # ■ Пропорциональное изменение размеров окружности,
    # # путем изменения ее радиуса (операции + - += -=).

    def __add__(self, num: int):
        return Circle(self.radius + num)

    def __sub__(self, num: int):
        return Circle(self.radius - num)

    def __iadd__(self, num: int): # Я только вот так и не понял, а где эту шнягу использовать? -= я даже не сделал ибо
        self.radius += num # вообще не понимаю зачем она тут нужна
        self.length = self.radius * 3.14 * 2

    def __str__(self):
        return f"{self.radius}"

    def show_info(self):
        print(f"Радиус - {self.radius}, Длина окружности - {self.length}")

a = Circle(123)
b = Circle(222)

print(a == b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

print()

(a + 100).show_info()
(b + 100).show_info()

print()

(a - 100).show_info()
(b - 100).show_info()

# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

print('\nЗадание 2\n') # Это задание я не понял как делать от слова совсем.
#                      Буду рад если покажете решение, а то 2 часа сидел - и безтолку

# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# Домашнее задание
# 1
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).

print('\nЗадание 3\n')

class Airplane:
    def __init__(self, type: str, passengers: int):
        self.type = type
        self.passengers = passengers

    # # ■ Проверка на равенство типов самолетов (операция
    # # = =);

    def __eq__(self, other: 'Airplane') -> 'Airplane':
        return Airplane(self.passengers,self.type == other.type)

    # # ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);

    # Только не совсем понимаю зачем здесь += и -=

    def __add__(self, other: 'Airplane') -> 'Airplane':
        return Airplane(self.type,self.passengers + other.passengers)

    def __sub__(self, other: 'Airplane') -> 'Airplane':
        return Airplane(self.type,self.passengers - other.passengers)

    # ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
    # < <= >=).

    def __gt__(self, other: 'Airplane') -> 'Airplane':
         return Airplane(self.type,self.passengers > other.passengers)

    def __lt__(self, other: 'Airplane') -> 'Airplane':
         return Airplane(self.type,self.passengers < other.passengers)

    def __le__(self, other: 'Airplane') -> 'Airplane':
         return Airplane(self.type,self.passengers <= other.passengers)

    def __ge__(self, other: 'Airplane') -> 'Airplane':
         return Airplane(self.type,self.passengers >= other.passengers)

    def __str__(self):
        return f"{self.passengers}"

a = Airplane('Боинг', 123)
b = Airplane('Сухой', 1000)
c = Airplane('Боинг', 2345)

print(a == b)
print(a == c)

print()

print(a + b)
print(a - b)

print()

print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

print('\nЗадание 4\n')

class Flat:
    def __init__(self, square: int, price: int):
        self.square = square
        self.price = price

    # # ■ Проверка на равенство площадей квартир (операция
    # # ==);
    def __eq__(self, other: 'Flat') -> 'Flat':
        return Flat(self.price,self.square == other.square)

    # # ■ Проверка на неравенство площадей квартир (операция !=);

    def __ne__(self, other: 'Flat') -> 'Flat':
        return Flat(self.price,self.square != other.square)

    # # ■ Сравнение двух квартир по цене (операции > < <= >=).

    def __gt__(self, other: 'Flat') -> 'Flat':
        return Flat(self.square,self.price > other.price)

    def __lt__(self, other: 'Flat') -> 'Flat':
        return Flat(self.square,self.price < other.price)

    def __le__(self, other: 'Flat') -> 'Flat':
        return Flat(self.square,self.price <= other.price)

    def __ge__(self, other: 'Flat') -> 'Flat':
        return Flat(self.square,self.price >= other.price)

    def __str__(self):
        return f"{self.price}"

Room_1 = Flat(100,654)
Room_2 = Flat(321,6459)
Room_3 = Flat(100,321)

print(Room_1 == Room_2)
print(Room_1 == Room_3)

print()

print(Room_1 != Room_2)

print()

print(Room_1 > Room_2)
print(Room_1 < Room_2)
print(Room_1 <= Room_2)
print(Room_1 >= Room_2)