"""6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
"""
items_number = int(input('Введите количество товаров: '))
items_dict = []
i = 0
while i < items_number:
    item_name = input(f'\nВведите имя {i+1}-го товара: ')
    item_price = input(f'Введите цену для {item_name}: ')
    item_qty = input(f'Введите количество {item_name}: ')
    item_id = input(f'Введите единицу измерения для {item_name}: ')
    item = (i+1, {'название': item_name, 'цена': item_price, 'количество': item_qty, 'ед': item_id})
    items_dict.append(item)
    i += 1
print(items_dict)
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий товаров.
result_names = []
result_prices = []
result_qty = []
result_id = []
for item in items_dict:
    result_names.append(item[1].get('название'))
    result_prices.append(item[1].get('цена'))
    result_qty.append(item[1].get('количество'))
    result_id.append(item[1].get('ед'))
result_dict = {'название': result_names, 'цена': result_prices, 'количество': result_qty, 'ед': result_id}
print(result_dict)