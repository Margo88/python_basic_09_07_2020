#1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

greeting = 'Всем приветики!'
name = 'Larisa'
surname = 'Guzeeva'
age = 61
weight = 82.3
growth = 168
print(f'{greeting} Меня зовут {name} {surname}.')
print(f'Мне {age} год, я вешу {weight} килограмм, а мой рост {growth} см')
answer = input('Хотите принять участие в нашей программе? ')
if answer.lower() == 'да':
    print('Супер! Заполните анкету: ')
    guest_name = input('Как Вас зовут? ')
    guest_age = int(input('Сколько Вам лет '))
    print(f'{guest_name}, добро пожаловать!')
else:
    print('Ой все')