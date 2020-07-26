"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
first_file = open('first_file.txt', 'w', encoding='UTF-8')
while True:
    content = input('Введите данные для записи в файл: ')
    first_file.write(content + '\n')
    if content == "":
        break
first_file.close()
