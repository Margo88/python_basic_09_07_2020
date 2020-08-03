"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def max_row(self):
        """метод для нахождения самого длинного списка в списке"""
        return max([len(row) for row in self.list_of_lists])

    def add_zero(self):
        """метод, создающий прямоугольную матрицу из списков разной длины путем добавления нолей в короткие списки"""
        matrix = self.list_of_lists[:]
        for row in matrix:
            while len(row) < self.max_row():
                row.append(0)
        return matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, _)) for _ in self.add_zero())

    def __add__(self, other):
        """только для матриц одного размера"""
        x = self.add_zero()
        y = other.add_zero()
        sum_list = []

        result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
        for r in result:
            sum_list.append(r)
        return Matrix(sum_list)

    # def __add__(self, other):
    # """Вариант решения для разноразмерных матриц"""
    #     if len(self.add_zero()) > len(other.add_zero()):
    #         max_list = self.add_zero()
    #         min_list = other.add_zero()
    #     else:
    #         max_list = other.add_zero()
    #         min_list = self.add_zero()
    #     while len(min_list) != len(max_list):
    #         min_list.append([0])
    #
    #     sum_list = []
    #     i = 0
    #     while i < len(max_list):
    #         max_v = max_list[i]
    #         min_v = min_list[i]
    #         if len(max_list[i]) < len(min_list[i]):
    #             max_v = min_list[i]
    #             min_v = max_list[i]
    #         pre_result = list(map(sum, zip(max_list[i], min_list[i]))) + max_v[len(min_v):]
    #         sum_list.append(pre_result)
    #         i += 1
    #     return Matrix(sum_list)


a = Matrix([[1, 3, 8], [4, 3, 6, 1], [4, -5, 6]])
b = Matrix([[4, 0, 1, 6], [8, 8, 2, 11], [5, 6, 4]])
print(a, '\n')
print(b, '\n')
print(a + b)