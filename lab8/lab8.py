#Дана целочисленная матрица размера 6х9. Найти матрицу получающуюся из данной:
#a) перестановкой столбцов - первого с последним, второго с предпоследним и т.д.
# https://ivtipm.github.io/Programming/Glava20/index20.htm#z676

__author__ = "Гурбатов Владислав"


import source


n = int(input("Введите размер матрицы: "))
# создание рандомной матрицы от 0 до 100 размером nxn
a = source.create_matrix(n)

#вывод изначальной матрицы матрицы
print("изначальная матрица:")
source.print_massive(a,n)
a = source.matrowchange(a, n)
#вывод полученной матрицы
print("получившаяся матрица:")
source.print_massive(a, n)

