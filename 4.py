"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


with open('test4.txt', 'r', encoding='utf-8') as f:
    with open('test4_ru.txt', 'w', encoding='utf-8') as f_ru:
        list_numerals = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
        for line in f:
            main_line = line.split(' ')[1:]
            main_line.insert(0, list_numerals[int(main_line[1])])
            f_ru.write(' '.join(main_line))
f.close()
f_ru.close()
