magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# # Задание 1. class Phonebook:...
# # add_contact(name, phone_number) -> None (Добавляем контакт в книгу)
# # remove_contact(name) -> None (Удаляет контакт если он был, иначе выводит сообщение об ошибке)
#
# # update_contact(name, phone_number) -> None (Изменяет номер телефона у контакта с именем name)
#
# # get_contact(name) -> str(phone_number) (Возвращает номер телефона по имени)
# # get_all_contacts() -> list (Возвращает список всех записей)
#
# print('\nЗадание 1\n')
#
# class Phonebook:
#     def __init__(self):
#         self.contacts = {}
#
#     def add(self,name,telephone):
#         self.contacts[name] = telephone
#         print('Contact has been added')
#
#     def get_one(self,name):
#         return self.contacts[name]
#
#     def remove(self,name):
#         if name in self.contacts:
#             del self.contacts[name]
#             print('Contact has been deleted')
#         else:
#             print('There are no contacts with this name')
#
#     def all_contacts(self):
#         # Это решение я подглядел у вас на уроке
#         lst_contacts = []
#         for key, value in self.contacts.items():
#             lst_contacts.append([key,value])
#         return  lst_contacts
#
# Phone_book = Phonebook()
# Phone_book.add('Илья', '88005553535'),Phone_book.add('Алёша', '1234567891')
# Phone_book.add('Бобер Польский', '1478963251'),Phone_book.add('Трактор', '79695697423')
#
# print(),print(Phone_book.all_contacts())
# print(),print(Phone_book.get_one('Илья'))
#
# print(),Phone_book.remove('Илья')
# print(),print(Phone_book.all_contacts())
#
# # Релизуйте класс Timer, поддерживающий следующие методы:
# #
# # start(): запускает таймер
# # stop(): останавливает таймер
# # reset(): сбрасывает таймер на ноль
# # elapsed_time(): возвращает время, прошедшее с момента запуска таймера, в секундах
#
# print('\nЗадание 2\n') # Это задание сегодня вы показывали
#
# import time
#
# class Timer:
#     def __init__(self):
#         self.time = 0
#         self.start_time = None
#
#     def format_time(self, time):
#         return  round(time,3)
#     def start(self):
#         if not self.start_time:
#             self.start_time = time.time()
#         else:
#             print('The timer is already running')
#     def stop(self):
#         if self.start_time:
#             self.time = self.format_time(time.time() - self.start_time)
#         else:
#             print('The timer has not been started')
#     def reset(self):
#         self.start_time = None
#
#     def elapsed(self):
#         if self.start_time:
#             return self.format_time(time.time() - self.start_time)
#         return 'The timer has not been started'
#
# timer = Timer()
# timer.start()
# [i for i in range(1234567)]
# timer.stop()
# print(timer.time)
