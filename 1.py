'''
Реализовать функцию, 
принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у 
пользователя, предусмотреть обработку ситуации 
деления на ноль.
'''
# функция через цикл while
def my_funk_div (a,b):
    while True:
        if (a == 0 or b == 0):
            print('Деление на 0! Попробуйте снова')
            a = int(input('Первое: '))
            b = int(input('Второе: '))
        else:
            divede = float(a / b)
            break
    print(divede)

x = int(input('Первое: '))
y = int(input('Второе: '))
my_funk_div(x ,y )

print(' Второй вариант решения, который мне "не зашел"...но как я понял..именно этот "формально" верный')
# функция через try и except
def func_div(*args):
    try:
        param_1 = int(input('Первое: '))
        param_2 = int(input('Второе: '))
        divede = param_1 / param_2
    except ValueError:
        return 'Ошибка значения '
    except ZeroDivisionError:
        return 'Ошибка. Нельзя делить на ноль! '
    return divede
print(f'Ваш результат деления:  {func_div()}')

