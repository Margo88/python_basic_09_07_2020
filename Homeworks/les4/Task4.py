"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

first_list = [18, 33, 94, 2, 18, 31, 7, 10, 10, 91, 94, 11, 2, 31]
result_list = [itm for itm in first_list if first_list.count(itm) < 2]

print(first_list)
print(result_list)

