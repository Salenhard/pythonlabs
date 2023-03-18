#Даны натуральное число n, действительные числа a1,..., an. Вычислить:
#(sqrt(ai)-ai)**2 
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136

import source

__author__ = "Влад Гурбатов"
assert source.sum_array([1]) == 0
assert source.sum_array([1,2,3,4,5,6]) == -10.5
assert source.sum_array([1,2,3,4,5]) == -7.5
assert source.sum_array([1,2,3,4,4]) == -7
# ввод размера массива
n = int(input("Введите размер массив: "))
a = source.create_array(n)
print("Данный массив:")
source.print_array(a)
print(f"Результат: {source.sum_array(a):.4f}")
