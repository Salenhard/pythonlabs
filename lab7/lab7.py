# Вычислить:
# i0->100 j0->100:(j-i+1)/(i+j)
# https://ivtipm.github.io/Programming/Glava10/index10.htm#z334


import source

__author__ = "Гурбатов Владислав"
# ввод
n = int(input("Введите кол-во итераций в 1 цикле: "))
m = int(input("Введите кол-во итераций во 2 цикле: "))
# цикл
s = source.sum_cicle(n, m)

print(f"Результат: {s}")
# тесты
assert source.sum_cicle(5, 2) == -0.15000000000000002
assert source.sum_cicle(100, 50) == -1183.2498173109102
assert source.sum_cicle(50, 100) == 1362.038928699253