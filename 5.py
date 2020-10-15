"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

import random
def get_sum(nums_str):
    sum = 0
    for num in nums_str:
        sum += int(num)
    return sum
if __name__ == "__main__":
    with open("test5.txt", 'w') as t1:
        num = random.randrange(10, 100)
        print(num)
        for num in range(num):
            number_for_write = random.randrange(10, 100)
            print(number_for_write)
            t1.write(str(number_for_write))
            t1.write(" ")
        t1.flush()
        with open("test5.txt", 'r') as t2:
            nums = t2.read().strip().split()
            sum_nums = get_sum(nums)
            print(f"Сумма всех чисел в списке: {sum_nums}")