# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Статические методы

# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод, который при вызове возвращает
# количество созданных объектов класса «Дробь».

print('\nЗадание 1\n')

class fractio:
    count = 0
    def __init__(self,numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        fractio.count =+ 1

    @staticmethod # Вот здесь реализовал
    def show_count():
        return fractio.count

    def change_fractio(self):
        self.numerator = int(input('Введите новое значение числителя: '))
        self.denominator = int(input('Введите новое значение знаменателя: '))

    def show(self):
        print(f'{self.numerator}/{self.denominator}')

    def plus_doing(self, another: "fractio"):
        print  ((self.numerator / self.denominator) + (another.numerator / another.denominator))

    def minus_doing(self, another: "fractio"):
        print((self.numerator / self.denominator) - (another.numerator / another.denominator))

    def multiply(self, another: "fractio"):
        print((self.numerator / self.denominator) * (another.numerator / another.denominator))

    def divide(self, another: "fractio"):
        print((self.numerator / self.denominator) / (another.numerator / another.denominator))


a = fractio(13, 23)
b = fractio(4,33)

a.show()
b.show()

print()

a.plus_doing(b)
a.minus_doing(b)
a.multiply(b)
a.divide(b)

print()

print('Счетчик: ',fractio.show_count()) # вот здесь вызвал

# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода

print('\nЗадание 2\n')

class convertation:
    count = 0
    @staticmethod
    def conv_cel_into_far(cel):
        convertation.count += 1
        return (9/5*cel+32)
    @staticmethod
    def conv_far_into_cel(far):
        convertation.count += 1
        return 5.0*(far - 32) / 9
    @staticmethod
    def show_count():
        return convertation.count

print(convertation.conv_cel_into_far(10))
print(convertation.conv_far_into_cel(10))
print('Счетчик: ',convertation.show_count())

# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины

print('\nЗадание 3\n')

class transfer_to_eng_system:
    # Из метрической системы в английскую
    @staticmethod
    def from_m_to_miles(metres):
        return metres / 1609
    @staticmethod
    def from_m_to_yards(metres):
        return metres / 0.9144
    @staticmethod
    def from_cm_to_foot(cm):
        return cm / 30.48
    @staticmethod
    def from_cm_to_inch(cm):
        return cm / 2.54

    # Из английской в метричную
    @staticmethod
    def from_miles_to_m(miles):
        return miles * 1609
    @staticmethod
    def from_yards_to_m(yards):
        return yards * 0.9144
    @staticmethod
    def from_foot_to_cm(foot):
        return foot * 30.48
    @staticmethod
    def from_inch_to_cm(inch):
        return inch * 2.54

# Из метрической системы в английскую
print(transfer_to_eng_system.from_m_to_miles(1000))
print(transfer_to_eng_system.from_m_to_yards(1000))
print(transfer_to_eng_system.from_cm_to_foot(1000))
print(transfer_to_eng_system.from_cm_to_inch(1000))

print()

# Из английской в метричную
print(transfer_to_eng_system.from_miles_to_m(1000))
print(transfer_to_eng_system.from_yards_to_m(1000))
print(transfer_to_eng_system.from_foot_to_cm(1000))
print(transfer_to_eng_system.from_inch_to_cm(1000))