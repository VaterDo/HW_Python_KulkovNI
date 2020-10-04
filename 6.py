'''
* Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей.

В кортеже должно быть два элемента — номер товара и словарь с параметрами 

(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, 
в котором каждый ключ — характеристика товара, например название, 
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''
good_num = 1
goods = list() #список кортежей. В Кортеже -> 2 элемента: 1. Номер; 2. Словарь хар-к
big_count = int(input('Введите общее кол-во товаров: ')) # проверка готовности
for t in range(big_count):
    # формирование структуры
    good_dict = dict(Наименование = input('Введите наименование: '), Цена = input('Введите стоимость: '), Колличесство = input('Введите кол-во: '), Ед_измерения = input('Введите ед.измерения: '))
    # формируем список по услвоию № + инфо о товаре: 
    info_to_good = (good_num, good_dict)
    goods.append(info_to_good)
    good_num += 1 # добавил счетчик
print('Ваша структура выглядит так:')
for i in goods:
    print(i)
# формируем аналитику товара.
name_list = []
price_list = []
quantity_list = []
unit_list = []
analytics = {}
# сам алгоритм формируем через обращению к текущему списку и его элементам в отдельности:
for num in range(len(goods)):
    name_list.append(goods[num][1][list(goods[0][1].keys())[0]])
    price_list.append(goods[num][1][list(goods[0][1].keys())[1]])
    quantity_list.append(goods[num][1][list(goods[0][1].keys())[2]])
    unit_list.append(goods[num][1][list(goods[0][1].keys())[3]])
analytics[list(goods[0][1].keys())[0]] = name_list
analytics[list(goods[0][1].keys())[1]] = price_list
analytics[list(goods[0][1].keys())[2]] = quantity_list
analytics[list(goods[0][1].keys())[3]] = list(set(unit_list))
print(f"Статистика по таблице товаров: {analytics}")
