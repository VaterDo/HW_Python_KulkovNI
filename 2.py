'''
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите 
в формате чч:мм:сс. 
Используйте форматирование строк.
'''

user_input = int(input('Введите время в секундах: '))
second = user_input
minuts = user_input // 60
hours = minuts // 60

print ('{:>02}:{:>02}:{:>02}'.format(hours, minuts % 60, second % 60))

# либо:
#print(f'{hours}:{minuts % 60}:{second % 60}')
