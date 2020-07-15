"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
while True:
    len_list = input('Укажите длину списка: ')
    if len_list.isdigit():
        len_list = int(len_list)
        break
    print('Ошибка ввода. Необходимо ввести число!')
i = 0
user_list = []
while i < len_list:
    user_list.append(input(f'Введите элемент №{i + 1}: '))
    i += 1
print(f'Исходный список: \n{user_list}\n')

j = 0
for i in range(int(len_list / 2)):
    user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    j += 2
print(f'Список с переставленными элементами: \n{user_list}')