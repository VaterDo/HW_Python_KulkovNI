"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open("test3.txt", 'r') as t:
    # выводим переменную и составляем список для работы из текста файла
    text = t.read()
    col_list = text.split('\n')
    # списки необходимы для единого вывода, что бы не спамить в переборе for-ов (см. циклы далее по коду)
    coins = []
    colleg_with_min = []
    # алгоритм сбора информации о з\п и анализа размера з\п:
    for i in col_list:
        elems_in_list = i.split()
        # print (elems_in_list)
        int_elems = int(elems_in_list[-1])
        coins.append(int_elems)
        for elem in elems_in_list:
            if elem.isdigit() and int(elems_in_list[-1]) < 20000:
                colleg_with_min.append(elems_in_list[0])
    # вывод о сотрудниках с зп < 20 000 
    print(f"Сотрудники, которые получают оклад, менее 20 000 рублей: {'; '.join(colleg_with_min)}")
# ищем среднюю з\п
import statistics
average = statistics.mean(coins)
print(f'Средняя заработная плата по Вашему списку сотрудников = {int(average)} рублей')
