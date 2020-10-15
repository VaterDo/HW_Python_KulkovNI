"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def get_sum_lessons(list_subject):
    """
    принимает список строк, содержащих информацию о предмете,
    извлекает элементы, содержащие числовые значения (колличество занятий)
    и возвращает их сумму (общее число занятий)
    :param list_subject: список строк, содержащих информацию о предмете
    :return: sum_lessons: сумма общего числа занятий по предмету
    """
    lessons = []
    for el in list_subject:
        if el.isdigit():
            lessons.append(int(el))
    sum_lessons = sum(lessons)
    return sum_lessons


if __name__ == "__main__":
    with open("test6.txt", "r") as t:
        text = t.readlines()
        total_number_of_lessons = {}
        for line in text:
            new_line = line.replace("(", " ")
            list_line = new_line.strip().split()
            sum_ = get_sum_lessons(list_line)
            subject = list_line[0].replace(":"," ").strip()
            total_number_of_lessons[subject] = sum_
        print(total_number_of_lessons) 