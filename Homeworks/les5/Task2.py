"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
lines = 0
with open('second_file.txt', 'r', encoding='UTF-8') as count_file:
    for line in count_file:
        lines += 1
        words = len(line.split(' '))
        if line == '\n':
            words = 0
        print(f'В строке №{lines} содержится {words} слов')
print(f'В файле всего {lines} строк')




