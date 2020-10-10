'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: 
(выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений 
необходимо запускать скрипт с параметрами.
'''
from sys import argv
script_name, payment, time, prize = argv

print('Имя скрипта: ', script_name)
print('Первый параметр (сумма оклада): ', payment)
print('Второй параметр (время): ', time)
print('Третий параметр (премия)', prize)

all_pay = int(payment)*int(time)+int(prize)

print(f'Ваша з/п: {all_pay}')
