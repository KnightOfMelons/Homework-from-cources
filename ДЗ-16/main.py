# Реализовать иерархию классов:
# Наземный транспорт -> колесный транспорт
# 				   -> гусеничный транспорт
# 				   -> транспорт на воздушных подушках

class land_transport: # Не знаю, сделал ли я правильно иерархию, но я также снизу прикрутил вывод значений классов
    def models(self):
        return ('Колесный транспорт', 'Гусеничный транспорт', 'Транспорт на воздушных подушках')

class wheel_transport(land_transport):
    def models(self):
        return ('Lada Granta','Lada Vesta','UAZ Patriot','BARGUZIN GAZ 22177','AURUS Komendant')

class track_transport(land_transport):
    def models(self):
        return ('T-34','T-34-85','Т-90','T-95','T-54/55')

class air_cushion_transport(land_transport):
    def models(self):
        return ('ГАЗ-16А','DONAR M-10','Grand Touring Hovercraft (GTH)','Volkswagen Aqua','VonMercier Arosa')

def show_metod(cls): # Вот это отвечает за вывод информации из классов
    print(cls().models())

# Вот так изначально было в интернете, тут выводило название класса, создает экземпляр класса и проходит по методу test
# def test_method(cls):
#     print(cls)
#     print(cls().test())

print('\nТипы наземного транспорта: ', end = ' ')
show_metod(land_transport)

print('\nМодельный ряд колесного траспорта: ', end = ' ')
show_metod(wheel_transport)

print('\nМодельный ряд гусечного траспорта: ', end = ' ')
show_metod(track_transport)

print('\nМодельный ряд транспорта на воздушной подушке: ', end = ' ')
show_metod(air_cushion_transport)
