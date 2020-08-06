"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте
его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input("Введите делимое: ")
b = input("Введите делитель: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyError("Zero!")
except ValueError:
    print("not a number")

except MyError as mr:
    print(mr)
else:
    print(a/b)