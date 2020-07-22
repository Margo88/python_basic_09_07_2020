"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

# import math
#
# def fact(n):
#     for i in range(1, n + 1):
#         yield math.factorial(i)

while True:
    user_number = input('Введите число: ')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print('Ошибка ввода')

def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial

for el in fact(user_number):
    print(el)

