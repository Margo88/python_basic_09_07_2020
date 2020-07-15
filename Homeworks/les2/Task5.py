"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
rating = [8, 6, 5, 5, 2, 2]
print(f'Исходный набор чисел: {rating}')
print('Для выхода введите "Q"')
while True:
    user_number = input('Введите новый элемет рейтинга: ')
    if user_number.upper() == 'Q':
        break
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number in rating:
            count = rating.count(user_number) #посчитаем одинаковые символов, равные введенному пользователем
            position = rating.index(user_number) #найдем его индекс
            rating.insert(position+count, user_number) #и внесем в список после одинаковых
        else:
          rating.append(user_number)
          rating.sort(reverse = True)
        print(f'Результат: {rating}')
    else:
        print('Ошибка ввода!')