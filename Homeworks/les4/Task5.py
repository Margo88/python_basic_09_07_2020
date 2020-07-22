"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

even_list = [number for number in range(100, 1001) if not number & 1]

def mult(prev_num, num):
    return prev_num * num

print(even_list)
print(reduce(mult, even_list))