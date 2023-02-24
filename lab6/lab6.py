# Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:
# удовлетворяющих условию a[k] < (a[k-1] - a[k+1])/2
# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178

import source
 
__author__ = "Влад Гурбатов"


# ввод значений
n = int(input("Введите размер массива: "))
a = source.create_mas(n)

print("Результат: ", source.print_massive(source.array_filter(a,n)))
