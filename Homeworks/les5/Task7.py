"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
 убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('seventh.txt', 'r', encoding='UTF-8') as in_file:
    content = in_file.readlines()
    firm_dict = {}
    profit_sum = 0
    profit_count = 0
    for line in content:
        line_list = line.split(' ')
        profit = int(line_list[2]) - int(line_list[3].replace('\n',''))
        firm_dict[line_list[0]] = profit
        if profit > 0:
            profit_sum += profit
            profit_count += 1
        print(f'Прибыль {line_list[1]} {line_list[0]} составила: {profit} рублей')
    average_profit = int(profit_sum/profit_count)
    avg_profit_dict = {'Средняя прибыль': average_profit}
    print(f'\nСредняя прибыль составила: {average_profit}')

result_list = [firm_dict, avg_profit_dict]

with open('seventh.json', 'w', encoding='UTF-8') as js_file:
    json.dump(result_list, js_file)