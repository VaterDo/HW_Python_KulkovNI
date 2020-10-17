"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight_of_asphalt(self, mass_one_sqr_meter, thickness_fabric):
        length_road = self._length
        width_road = self._width
        mass = length_road * width_road * mass_one_sqr_meter * thickness_fabric
        return mass


if __name__ == "__main__":
    road = Road(5000, 20)
    full_mass = road.get_weight_of_asphalt(25, 0.05)
    print(f"Масса асфальта для покрытия всего дорожного полотна составит {int(full_mass)} т")