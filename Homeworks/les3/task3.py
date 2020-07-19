"""3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_func(arg1, arg2, arg3):
    min = arg1
    if arg2 < min:
        min = arg2
    elif arg3 < min:
        min = arg3
    sum = arg1 + arg2 + arg3 - min
    return sum

#Функция, запрашивающая у пользователя чило и обрабатывающая исключение
def input_and_check(position):
    while True:
        try:
            number = input(f'Введите {position} число: ')
            number = int(number)
            return number
            break
        except ValueError:
            print('Ошибка ввода. Необходимо ввести число')

a = input_and_check('первое')
b = input_and_check('второе')
c = input_and_check('третье')

print(f'Сумма двух наибольших чисел из трех = {my_func(a, b, c)}')

