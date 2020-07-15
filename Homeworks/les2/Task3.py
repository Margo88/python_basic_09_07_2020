"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
while True:
    user_number = input('Введите порядковый номер месяца: ')
    if user_number.isdigit():
        user_number = int(user_number)
        if int(user_number) <= 12:
            break
    print('Ошибка ввода. Необходимо ввести число от 1 до 12.')
# Решение с использованием списка:
seasons_list = [['Зима', 1, 2, 12], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
i = 0
for season in seasons_list:
    if user_number in seasons_list[i]:
        print(f'Время года: {seasons_list[i][0]}')
    i += 1
# Решение с использованием словаря:
seasons_dict = {
    'Зима': [1, 2, 12],
    'Лето': [6, 7, 8],
    'Весна': [4, 5, 3],
    'Осень': [9, 10, 11]
}
for key in seasons_dict.keys():
    if user_number in seasons_dict[key]:
        print(f'Время года: {key}')