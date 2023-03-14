# Задание 1.
# Создайте класс Date, который хранит значение даты и предоставляет свойства для
# получения и установки даты. Используйте декораторы @property и @setter для реализации свойств.
# Установка новой даты должна быть логически защищена от неверного ввода. Также надо создать методы:
# 1. set_date() - должен производить валидацию введенной строки (например, "гггг-мм-дд") после
# чего устанавливать эту дату, как текущую
# 2. days_in_month() - должен возвращать количество дней в текущем месяце.
# 3. is_leap_year() - должен возвращать, является ли текущий год високосным.
# 4. next_day() - должен изменять текущую дату на один день вперед
# 5. __str__() - должен правильно отображать дату в строке

class Date: # Если что я объединил ваше решение на уроке и мое. А также на всякий случай исходное
    # решение свое я оставил внизу под этим заданием
    def __init__(self, year: int, month: int, day: int):
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def year(self) -> int:
        return self.__year
    @property
    def month(self) -> int:
        return  self.__month
    @property
    def day(self) -> int:
        return self.__day

    @year.setter
    def year(self, year: int):
        self.__year = year
    @month.setter
    def month(self, month: int):
        if 0 < month <= 12:
            self.__month = month
        else:
            print('\nМесяц должен быть от 1 до 12.\n')
    @day.setter
    def day(self, day: int):
        days = self.days_in_month()
        if 0 < day <= days:
            self.__day = day
        else:
            print('\nДень должен быть от 1 до 31.\n')

    def is_leap_year(self, year = None):
        year = year if year else self.__year
        if (self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0):
            return True
        else:
            return False

    def days_in_month(self, month = None, year = None):
        month = month if month else self.__month
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month in [4,6,9,11]:
            return 30
        elif month == 2 and self.is_leap_year(year):
            return 29
        else:
            return 28

    def next_day(self):
        if self.month == 2 and self.day == 28 and (self.year % 4 == 0 and self.year % 100 != 0
                                                     or self.year % 400 == 0):
            self.day = 29
            return self.day

        elif self.month == 2 and self.day == 28:
            self.day = 1
            return self.day

        elif (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 1) and self.day == 30:
            self.day = 1
            return self.day

        elif (self.month == 1 or self.month == 3 or self.month == 5
                               or self.month == 7 or self.month == 8 or self.month == 10
                               or self.month == 12) and self.day == 31:
            self.day = 1
            return self.day
        else:
            return self.day + 1

    def set_date(self, year_new: int, month_new: int,day_new: int):

        if month_new <= 0 or month_new > 12 or  day_new > 31 and (month_new == 1 or month_new == 3 or month_new == 5
                               or month_new == 7 or month_new == 8 or month_new == 10
                               or month_new == 12) or day_new > 30 and (month_new == 4 or month_new == 6
                                                                        or month_new == 9 or month_new == 1):
            print('Некорректно введенные данные')

        else:
            self.__year = year_new
            self.__month = month_new
            self.__day = day_new
            print(f"Отныне текущая дата: {self.__year, self.__month, self.__day}")


    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

print('\n=======','Не високосный год проверка','=======\n')

a = Date(2000,4,10)
print(a)
a.set_date(2010,6,10)
print(a.days_in_month())
print(a.is_leap_year())
print(a.next_day())


print('\n=======','Високосный год проверка','=======\n')

b = Date(2016,2,28)
print(b.days_in_month())
print(b.is_leap_year())
print(b.next_day())

print('\n=======','Странные данные','=======\n')

c = Date(-1000, 10,10)
c.set_date(-900,12,31)
print(c.days_in_month())
print(c.is_leap_year())
print(c.next_day())

# ====================================================================================================================
# ========================================== МОЁ СТАРОЕ РЕШЕНИЕ С УРОКА ==============================================
# ====================================================================================================================

# class Date:
#     def __init__(self, year: int, month: int, day: int):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def set_date(self, year_new: int, month_new: int,day_new: int):
#
#         if month_new <= 0 or month_new > 12 or  day_new > 31 and (month_new == 1 or month_new == 3 or month_new == 5
#                                or month_new == 7 or month_new == 8 or month_new == 10
#                                or month_new == 12) or day_new > 30 and (month_new == 4 or month_new == 6
#                                                                         or month_new == 9 or month_new == 1):
#             print('Некорректно введенные данные')
#
#         else:
#             print(f"Отныне текущая дата: {year_new, month_new, day_new}")
#             self.year = year_new
#             self.month = month_new
#             self.day = day_new
#


#     Тут у меня ошибка, я думал нужно вывести сколько дней у нас в памяти

#     @property
#     def days_in_month(self):
#         return (f"Количество дней в месяце: {self.day}")
#
#     @property
#     def is_leap_year(self):
#         if (self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0):
#             return True
#         else:
#             return False
#
#     @property
#     def next_day(self):
#         if self.month == 2 and self.day == 28 and (self.year % 4 == 0 and self.year % 100 != 0
#                                                      or self.year % 400 == 0):
#             self.day = 29
#             return self.day
#
#         elif self.month == 2 and self.day == 28:
#             self.day = 1
#             return self.day
#
#         elif (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 1) and self.day == 30:
#             self.day = 1
#             return self.day
#
#         elif (self.month == 1 or self.month == 3 or self.month == 5
#                                or self.month == 7 or self.month == 8 or self.month == 10
#                                or self.month == 12) and self.day == 31:
#             self.day = 1
#             return self.day
#         else:
#             return self.day + 1
#
# print('\n=======','Не високосный год проверка','=======\n')
#
# a = Date(2000,10,10)
# a.set_date(2010,12,31)
# print(a.days_in_month)
# print(a.is_leap_year)
# print(a.next_day)
#
# print('\n=======','Високосный год проверка','=======\n')
#
# b = Date(2016,2,28)
# print(b.days_in_month)
# print(b.is_leap_year)
# print(b.next_day)
#
# print('\n=======','Странные данные','=======\n')
#
# c = Date(-1000, 10,10)
# c.set_date(-900,12,31)
# print(c.days_in_month)
# print(c.is_leap_year)
# print(c.next_day)