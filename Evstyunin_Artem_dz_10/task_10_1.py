# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.



class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        matrix_list = []
        for line in self.my_list:
            line = str(line)
            elem = line.replace(',',' ').replace('[','| ').replace(']',' |')
            matrix_list.append(elem)
        return '\n'.join(matrix_list)

    def __add__(self, other):
        sum = []
        for line_1, line_2 in zip(self.my_list,other.my_list):
            sum_line = [elem_1 + elem_2 for elem_1,elem_2 in zip(line_1, line_2)]
            sum.append(sum_line)
        return Matrix(sum)



matrix = Matrix([[31,22],[37,43],[51,86]])
matrix_2 = Matrix([[22,31],[43,37],[86,51]])
matrix_3 = Matrix([[95,57],[28,154],[789,32]])
# print(matrix)
# print(matrix_2)
# print(matrix_3)
print(matrix + matrix_2 + matrix_3)
