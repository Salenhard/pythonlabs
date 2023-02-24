# Вычислить:
# i0->100 j0->100:(j-i+1)/(i+j)
# https://ivtipm.github.io/Programming/Glava10/index10.htm#z334


import source

__author__ = "Гурбатов Владислав"
n = int(input("Введите кол-во итераций в 1 цикле: "))
m = int(input("Введите кол-во итераций во 2 цикле: "))
s = source.sum_cicle(n, m)
# цикл

print(f"Результат: {s:.4f}")