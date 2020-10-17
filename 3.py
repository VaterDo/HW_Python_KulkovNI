"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""
income = {
        "wade": 20000,
        "bonus": 30000
    }


class Worker:
    name = "Никита"
    surname = "Кульков"
    position = "Админ-р проекта"
    _income = income


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        total_income = self._income
        return total_income["wade"] + total_income["bonus"]


if __name__ == "__main__":
    new_worker = Worker()
    print(new_worker.name)
    position_new_worker = Position()
    print(position_new_worker.position)
    full_name_new_worker = position_new_worker.get_full_name()
    print(full_name_new_worker)
    income_new_worker = position_new_worker.get_total_income()
    print(income_new_worker)