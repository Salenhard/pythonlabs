#Даны натуральное число n, действительные числа a1,..., an. Вычислить:
#(sqrt(ai)-ai)**2 
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136

import source

__author__ = "Влад Гурбатов"
# ввод размера массива
n = int(input("Введите размер массив: "))
a = source.create_array(n)
print(f"Результат: {source.array_sum(a,n):.4f}")
