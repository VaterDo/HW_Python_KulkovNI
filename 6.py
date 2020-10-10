'''
Реализовать два небольших скрипта: 
а) итератор, генерирующий целые числа, 
начиная с указанного, 
б) итератор, повторяющий элементы некоторого списка, 
определенного заранее.
Подсказка: использовать функцию count() и cycle() 
модуля itertools. Обратите внимание, что создаваемый 
цикл не должен быть бесконечным. Необходимо предусмотреть 
условие его завершения. 
Например, в первом задании выводим целые числа, 
начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, 
при котором повторение элементов списка будет прекращено.
'''
from itertools import count, cycle


def get_int_num(first_num, last_num):
    for num in count(first_num):
        if num > last_num:
            break
        else:
            yield num


def get_identical_list(any_list):
    iteration_сount = 0
    for elem in cycle(any_list):
        if iteration_сount > (len(any_list) - 1):
            break
        yield elem
        iteration_сount += 1


if __name__ == "__main__":
    example = list(get_int_num(5, 20))
    print(example)
    copy_example = list(get_identical_list(example))
    print(copy_example)