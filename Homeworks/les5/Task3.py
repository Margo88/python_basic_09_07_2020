"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
worker_dict = {}
low_salary_list = []
sum = 0
with open('third_file.txt', 'r', encoding='UTF-8') as workers_data:
    for worker in workers_data:
        key, value = worker.split()
        worker_dict[key] = value
        sum += int(value)
        if int(value) < 20000:
            low_salary_list.append(key)

print(f'Сотрудники с низкими зарплатами: {low_salary_list}')
print(f'Средняя зарплата: {sum/len(worker_dict.keys())}')