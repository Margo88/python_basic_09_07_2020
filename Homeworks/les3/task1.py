"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def my_div(arg1, arg2):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        result = arg1 / arg2
    except ValueError:
        return 'Ошибка ввода'
    except ZeroDivisionError:
        return 'Ошибка деления на ноль'
    return result

while True:
    print('Для выхода введите Q')
    a = input('Введите делимое: ')
    if a.upper() == 'Q':
        break
    b = input('Введите делитель: ')
    if b.upper() == 'Q':
        break
    print(f'Результат деления: {my_div(a, b)}')