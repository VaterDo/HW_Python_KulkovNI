'''
Программа принимает действительное положительное 
число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде ф
ункции my_func(x, y). 
При решении задания необходимо обойтись 
без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, 
предусматривающая использование цикла.
'''
def my_func_one (x, y):
	# задаем простой вариант через**
	return x**y

def my_func(x, y):
	# преобразование с помощью abs
	y = abs(y)
	# задаем цикл счетчика, и поочередно умножаем x на себя пока abs значение y не будет равно 0
	res_1 = 1
	while y > 0:
		res_1 *= x
		y -= 1
	res_2 = 1 / res_1
	return res_2
# вывод
if __name__ == "__main__":
	print(f'Вывод с помощью оператора "**": {my_func_one(2, -5)}')
	print(f'Вывод без помощи оператора "**": {my_func(2, -5)}')
	t = int(input('Введите положительное число'))
	i = int(input('Введите отрицательное число'))
	print(f'Вывод через input, с помощью оператора "**": {my_func_one(t, i)}')
	print(f'Вывод через input без помощи оператора "**": {my_func(t, i)}')
