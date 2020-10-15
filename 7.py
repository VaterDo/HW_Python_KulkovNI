"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
with open("test7.txt", "r") as t:
    count = 0
    all_revenue = []
    statistics = {}
    for line in t:
        list_line = line.strip().split()
        list_nums = []
        for elem in list_line:
            if elem.isdigit():
                list_nums.append(int(elem))
        profit = list_nums[0] - list_nums[1]
        if profit > 0:
            all_revenue.append(profit)
            statistics[list_line[0]] = profit
            count += 1
        else:
            statistics[list_line[0]] = profit
    average_profit = sum(all_revenue) // count
    dict_average_profit = dict(average_profit=average_profit)
    all_statistics = [statistics, dict_average_profit]
    with open("json_data.txt", "w") as jd:
        json.dump(all_statistics, jd)
