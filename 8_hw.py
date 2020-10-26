"""
ex_1_hw_8
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных.
"""

  class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(i)

        return [int(my_date[0]), int(my_date[1]), int(my_date[2])]

    @staticmethod
    def valid(day, month, year):
        mon1 = [1, 3, 5, 7, 8, 10, 12]
        mon2 = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # Здесь мы учитываем, что 31 число бывает только по определенным месяцам!
        if day == 31 and month in mon1 and 0 <= year <= 2020:
            return f'Вы ввели правильный формат даты {day}.{month}.{year}'
        elif 1 <= day <= 28 and month == 2 and 0 <= year <= 2020:  # Февраль проверяем на наличие 28 числа!
            return f'Вы ввели правильный формат даты {day}.{month}.{year}'
        elif 1 <= day <= 30 and month in mon2 and 0 <= year <= 2020:
            return f'Вы ввели правильный формат даты {day}.{month}.{year}'  # Тут проверяем остальные месяца!
        else:
            return f'Вы ввели неправильный формат даты {day}.{month}.{year}'
        # На самом деле еще надо проверять високосный год на 29 февраля! Наверно это следующий уровень скилла=)

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)[0]}.' \
               f'{Data.extract(self.day_month_year)[1]}.' \
               f'{Data.extract(self.day_month_year)[2]}'


Day = Data('04-10-2020')
print(Day)
print("Проверим дату на корректность! ")
d = input("Введите день ")
while not d.isnumeric():
    d = input("Введите день ")
m = input("Введите месяц ")
while not m.isnumeric():
    m = input("Введите месяц ")
y = input("Введите год ")
while not y.isnumeric():
    y = input("Введите год ")
print(Day.valid(int(d), int(m), int(y)))

print(f"My b-day is {Day.extract('20-10-1993')[0]}."
      f"{Day.extract('20-10-1993')[1]}."
      f"{Day.extract('120-10-1993')[2]}")

"""
ex_2_hw_8
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""
class DelZero:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def divide(num_1, num_2):
        try:
            return f"Результат деления {num_1 / num_2}"
        except ZeroDivisionError:
            return f"Нельзя делить на ноль!"

n1 = input("Введите первую цифру ")
while not n1.isnumeric():
    n1 = input("Введите первую цифру ")
n2 = input("Введите на какую цифру мы будем делить ? ")
while not n2.isnumeric():
    n2 = input("Введите на какую цифру мы будем делить ? ")
div = DelZero(int(n1), int(n2))
print(div.divide(int(n1), int(n2)))

"""
ex_3_hw_8
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только
чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список. Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не
фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
"""

class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        stop = 0
        print("В любой момент вы можете написать stop и набор чисел прекратится!")
        while stop != 1:
            try:
                v = (input('Введите цифру ')).lower()
                if v == 'stop':
                    stop += 1
                    print(f'Вы вышли! Текущий список цифр - {self.my_list} \n ')
                else:
                    self.my_list.append(int(v))
                    print(f'Текущий список цифр - {self.my_list} \n ')
            except ValueError:
                s = (input(f'Это не цифра! Попробуем еще раз!\n'
                           f'Если хотите выйти напишите stop ')).lower()
                if s == 'stop':
                    stop += 1
                    print(f'Вы вышли! Текущий список цифр - {self.my_list} \n ')
                else:
                    print("Вы не написали stop тогда продолжим!")


try_except = Error()
try_except.my_input()


"""
ex_4-5-6_8_Hw
ачните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
хранилище = {принтеры: [], сканеры: [], ксероксы: []}
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

class ValueNotCorrect(Exception):
    def __init__(self, msg):
        self.message = msg

class Warehouse:
    warehouse = {
        'printers': [],
        'scanners': [],
        'copiers': []
    }
    records_of_equipment = {
        1: {'printers': [], 'scanners': [], 'copiers': []},
        2: {'printers': [], 'scanners': [], 'copiers': []},
        3: {'printers': [], 'scanners': [], 'copiers': []}
    }

    def receiving_equipment(self, name_equip, cls_equip, num):
        try:
            if not self.validation_equip_nums(name_equip, num) == "Данные корректны":
                raise ValueNotCorrect("Ошибка при вводе данных")
            self.warehouse[name_equip].append({cls_equip.name: [cls_equip, num]})
        except ValueNotCorrect as error:
            print(error)

    def transfer_to_a_division(self, num_division, type_equip, cls_equip, num):
        self.records_of_equipment[num_division][type_equip].append([cls_equip, num])
        equip_in_wh = self.warehouse[type_equip]
        for equip in equip_in_wh:
            if cls_equip.name == list(equip.keys())[0]:
                num_equip_in_wh = equip[cls_equip.name][1]
                equip[cls_equip.name][1] = num_equip_in_wh - num

    def validation_equip_nums(self, name_equip, num):
        types_equipment = ['printers', 'scanners', 'copiers']
        if name_equip in types_equipment and isinstance(num, int):
            return "Данные корректны"
        return "Данные не корректны"

class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    color = False
    cartridge_included = False

    def __init__(self, name, amount_of_paper, cartridge_included, color):
        super().__init__(name)
        self.amount_of_paper = amount_of_paper
        self.cartridge_included = cartridge_included
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed


class Copier(OfficeEquipment):
    def __init__(self, name, type_print, copy_permission):
        super().__init__(name)
        self.type_print = type_print
        self.copy_permission = copy_permission


scanner_1 = Scanner("HP", 200)
warehouse_1 = Warehouse()
print(warehouse_1.validation_equip_nums("hy", 9))
print(scanner_1.name)
warehouse_1.receiving_equipment("scanners", scanner_1, 10)
print(warehouse_1.warehouse)
printer_1 = Printer("Xerox", 400, True, False)
warehouse_1.receiving_equipment("printers", printer_1, 5)
print(warehouse_1.warehouse)
warehouse_1.transfer_to_a_division(2, "scanners", scanner_1, 6)
print(warehouse_1.warehouse)
print(warehouse_1.records_of_equipment)
warehouse_1.receiving_equipment("printer", printer_1, 5)


"""
ex_7_9_hw
Реализовать проект «Операции с комплексными числами».
 Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    """
    Класс, хранящий комплексное число.
    принимает позиционные параметры:
    real_part -- вещественная часть
    imaginary_part -- мнимая часть
    аргумент класса imaginary_unit хранит мнимую единицу
    """
    imaginary_unit = 1j

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def get_complex_num(self):
        return self.real_part + self.imaginary_part * self.imaginary_unit

    def __add__(self, other):
        return self.real_part + other.real_part + self.imaginary_unit * (self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        augend = (self.real_part * other.real_part - self.imaginary_part * other.imaginary_part) * self.imaginary_unit
        second_summand = (self.imaginary_part * other.real_part + self.real_part * other.imaginary_part) * self.imaginary_unit
        return augend + second_summand


complex_num_1 = ComplexNumber(1, 3)
print(complex_num_1.get_complex_num())
complex_num_2 = ComplexNumber(3, 2)
print(complex_num_2.get_complex_num())
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)