'''
Для чисел в пределах от 20 до 240 найти числа, 
кратные 20 или 21. 
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''

from random import randrange
new_list = [elem for elem in [randrange(20, 241) for i in range(30)] if elem % 20 == 0 or elem % 21 == 0]
print(new_list)

