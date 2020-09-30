'''
Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % 
относительно предыдущего. Требуется определить номер дня, 
на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и 
выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''
# результат в 1ый день
a = int(float(input("Введите 'км' в первый день: ")))
b = int(float(input("Введите желаемый результат в 'км': ")))
#запускаем цикл с учетом счетчика (важно не забыть зафиксить результат за сутки)
score_at_day = a
i = 0
while a < b:
    #выводим результат чуть раньше, для корректности подсчета
    print (f'В {i}-й день пробежал {a} км')
    a += score_at_day
    i += 1
    #выводим итоговый результат
    if a == b:
        print(f'В {i}-й день треиноровок - достигнете желаемого результата, и пробежите {a} км')
    elif a > b:
        print(f'В {i}-й день треиноровок Вы достигнете желаемого результата, и пробежите даже больше запланированного на {a - b} км')
    
