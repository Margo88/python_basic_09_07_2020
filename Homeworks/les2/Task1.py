"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно в программе.
"""
my_list = [False, ('hostname', 'location'), 3.14, 'Python', 0x11, -273.15, 'Каспийский груз', ['Mercury', 'Venus', 'Earth', 'Mars'], {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}]
i = 0
while i < len(my_list):
    print(my_list[i])
    print(type(my_list[i]),'\n')
    i += 1