"""1. Создать класс TrafficLight (светофор) и определить 
у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: 
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.Задачу можно усложнить, реализовав проверку порядка режимов, 
и при его нарушении выводить соответствующее сообщение и завершать скрипт. 
"""
# импорт модуля таймера цвета
import time
# создание класса
class TrafficLight():
	__color = 'red'
	# вводим метод и обозначаем его функционал
	def running (self):
		dote_to_run = input('Press ENTER, for running your traffic lighter, or enter "q" to exit: ')
		while dote_to_run == '':
			print(f'{TrafficLight.__color} color')
			time.sleep(7)
			TrafficLight.__color = 'yellow'
			print(f'{TrafficLight.__color} color')
			time.sleep(1.5)
			TrafficLight.__color = 'green'
			print(f'{TrafficLight.__color} color')
			time.sleep(5)
			TrafficLight.__color = 'red'
			print(f'{TrafficLight.__color} color\n')
			dote_to_run = input('Press ENTER to restart your traffic lighter, or enter "q", to exit: ')
# выводим его экземпдяр в виде переменной
sv_run = TrafficLight()
sv_run.running()
"""
не совсем понял, зачем вводить дополнительную провекру порядка переключения, 
если цвето задается в методе...и идет четко по по заданной в нем иерархии и порядке...
в целом проверка в представленном варианте была бы такой: 
if not TrafficLight.__color == 'red'
	print('Not correct choice light. Exit from program! ')
 	exit()	
else:
 	print(f'{TrafficLight.__color} color')
 	time.sleep(7)
и далее по аналогии
"""



