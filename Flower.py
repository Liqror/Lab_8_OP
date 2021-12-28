class Flower:
    def __init__(self, name, color, cost, count):
        self.name = name
        self.color = color
        self.cost = cost
        self.count = count

    def __str__(self):
        params = f'Название: {self.name} Цвет: {self.color} Цена: {self.cost} Количество: {self.count}'
        return params


pion = Flower('пион', 'розовый', 500, 10)
tulip = Flower('тюльпан', 'белый', 700, 12)
rosa = Flower('роза', 'красная', 600, 23)

dict_of_flowers = {pion.name: {'Название: ': pion.name,
                               'Цвет: ': pion.color,
                               'Цена: ': pion.cost,
                               'Количество: ': pion.count},
                   tulip.name: {'Название: ': tulip.name,
                                'Цвет: ': tulip.color,
                                'Цена: ': tulip.cost,
                                'Количество: ': tulip.count},
                   rosa.name: {'Название: ': rosa.name,
                               'Цвет: ': rosa.color,
                               'Цена: ': rosa.cost,
                               'Количество: ': rosa.count},

                   }



