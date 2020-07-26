"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

number_str = input('Введите числа через пробел: ')
sum = 0

with open('fifth.txt', 'w') as in_file:
    in_file.write(number_str)

with open('fifth.txt', 'r') as out_file:
    number_list = (out_file.read()).split(' ')

for number in number_list:
    sum += int(number)

print(f'Сумма введенных чисел равна: {sum}')
