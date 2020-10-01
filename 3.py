'''
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict. 
'''
# задаем список и словарь
mounth_list = [12,1,2,3,4,5,6,7,8,9,10,11]
mounth_dict = {
	"Зима":(1,2,12),
	"Весна":(3,4,5),
	"Лето":(6,7,8),
	"Осень":(9,10,11)
}
# проверяем пользовтельскую готовность
choise = input('Выберите ход программы -> через список (тип - list) или словарь (тип - dict)\nанглийская буква: "l" - поведет программу по "списку", а любой другой символ - по "словарю"')
# запуск кода по выбору пользователя
if choise == "l":
	user_input_list = int(input('Введите номер месяца от 1 до 12: '))
	if user_input_list in mounth_list[:3]:
		print(f'Вы ввели {user_input_list}, это зимний месяц')
	elif user_input_list in mounth_list[3:6]:
		print(f'Вы ввыели {user_input_list}, это весенний месяц')
	elif user_input_list in mounth_list[6:9]:
		print(f'Вы ввели {user_input_list}, это летний месяц')
	elif user_input_list in mounth_list[9:]:
		print(f'Вы ввели {user_input_list}, это осенний месяц')
else:
    user_input_dict = int(input('Введите номер месяца от 1 до 12: '))
    if user_input_dict in mounth_dict["Зима"]:
        print(f'Вы ввели {user_input_dict}, это зимний месяц')
    elif user_input_dict in mounth_dict["Весна"]:
	    print(f'Вы ввыели {user_input_dict}, это весенний месяц')
    elif user_input_dict in mounth_dict["Лето"]:
	    print(f'Вы ввели {user_input_dict}, это летний месяц')
    elif user_input_dict in mounth_dict["Осень"]:
        print(f'Вы ввели {user_input_dict}, это осенний месяц')