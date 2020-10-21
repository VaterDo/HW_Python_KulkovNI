"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, title):
        self.title = title


class Coat(Clothes):
    def __init__(self, title,  size):
        super().__init__(title)
        self.size = size

    @property
    def get_fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 1)


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    @property
    def get_fabric_consumption(self):
        return round(2 * self.height + 0.3, 1)


coat = Coat("Пальто", 46)
suit = Suit("костюм", 190)
print(coat.get_fabric_consumption)
print(suit.get_fabric_consumption)

