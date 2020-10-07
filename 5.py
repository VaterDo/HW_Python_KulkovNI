'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, 
разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить 
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
# задаем функцию сложения
def func_user_sum (count_user_list):
    num_list = []
    for i in count_user_list:
        i = int(i)
        num_list.append(i)
    sum_all_list = sum(num_list)
    return sum_all_list
# задаем алгоритмы проверки списка  
if __name__ == "__main__":
    count = 0
    bigger_sum = 0
    usage = input('Нажмите "enter" для запуска. Или введите "q" для завершения\n') # проверка готовности
    if usage == '':
        print('Program is started')
        while True:
            user_input = input('Введитe числа через пробел. Для выхода введите "q"\n').split() # формирование списка
            # алгоритм проверки по списку
            if user_input == 'q':
                print('Завершение программы.''\n'f'Общая сумма == {bigger_sum}')
                break
            # в случае окончания q отделяем его от списка и передаем в функцию только числа в строчном значении
            elif user_input[len(user_input) - 1] == 'q':
                new_user_input = user_input[:(len(user_input) -1)]
                sum_new_user_input = func_user_sum(new_user_input)
                bigger_sum += sum_new_user_input
                print('Завершение программы.''\n'f'Общая сумма == {bigger_sum}')
                break
            # наиболее простая часть алгоритма. Ведет подсчет - через вызов ранее написанной функции
            else:
                if count == 0:
                    bigger_sum = func_user_sum(user_input)
                    print(f'Общая сумма == {bigger_sum}')
                    count += 1
                else:
                    bigger_sum += func_user_sum(user_input)
                    print(f'Общая сумма == {bigger_sum}')
                    count += 1
    elif usage == 'q':
        print('Program was not started', f'Сумма не рассчитана и равна == {bigger_sum}', sep='\n')