"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

eng_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

file_rus = open('fourth_file_rus.txt', 'w', encoding='UTF=8')

with open('fourth_file.txt', 'r', encoding='UTF-8') as file:
    for eng_line in file:
        line_list = eng_line.split(' — ')
        rus_line = eng_dict[line_list[0]], line_list[1]
        file_rus.write(' — '.join(rus_line))

file_rus.close()



