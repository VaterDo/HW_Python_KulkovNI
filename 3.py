'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
# вводим число
n = input('Введите любое число от 1 до 9: ')
# задаем оставшиеся переменные выражения
param_1 = n
param_2 = n+n # *2
param_3 = n+n+n # *3
# преобразование в int
param_int_1 = int(param_1)
param_int_2 = int(param_2)
param_int_3 = int(param_3)
# сложение и вывод чере f'
sum_param = (param_int_1 + param_int_2 + param_int_3)
print (f'{param_int_1} + {param_int_2} + {param_int_3} = {sum_param}')