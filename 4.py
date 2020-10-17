"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = False
    speed = 100
    name = "Auto"
    color = "gray"

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if TownCar.speed > 60:
            return "Вы превысили скорость"
        return self.speed


class WorkCar(Car):

    def show_speed(self):
        if WorkCar.speed > 40:
            print("Вы превысили скорость")
        return self.speed


class PoliceCar(Car):
    is_police = True


if __name__ == "__main__":
    car = Car()
    print(car.color, car.name, car.speed)
    town_car = TownCar()
    print(town_car.name)
    town_car.name = "KIA"
    print(town_car.name)
    town_car.go()
    town_car.turn("лево")
    print(town_car.speed)
    town_car.speed = 70
    print(town_car.show_speed())
    police_car = PoliceCar()
    print(police_car.is_police)
    town_car.speed = 30
    print(town_car.speed)
    town_car.stop()
    print(town_car.is_police)