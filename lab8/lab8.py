#Дана целочисленная матрица размера 6х9. Найти матрицу получающуюся из данной:
#a) перестановкой столбцов - первого с последним, второго с предпоследним и т.д.
# https://ivtipm.github.io/Programming/Glava20/index20.htm#z676


import numpy as np


__author__ = "Гурбатов Владислав"


def print_massive(a:list, n:int):
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j], " ", end='')
        print()
        

def matrowchange(a:list, n:int):
    """Меняет колонны матрицы местами 1 с послденим и т.д."""
    b = np.zeros(n)
    for i in range(n//2):
        b[0:n] = a[0:n, i]
        a[0:n, i] = a[0:n, n-i-1]
        a[0:n, n-i-1] = b[0:n]
    return a

def create_array(n:int):
    return np.random.randint(0, 100, size = (n, n))

n = int(input("Введите размер матрицы: "))
# создание рандомной матрицы от 0 до 100 размером nxn
a = create_array(n)

#вывод изначальной матрицы матрицы
print("изначальная матрица:")
print_massive(a,n)
a = matrowchange(a, n)
#вывод полученной матрицы
print("получившаяся матрица:")
print_massive(a, n)
