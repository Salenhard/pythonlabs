#Вычислить:
# i**2/(i**2 + 2*i + 3)
#https://ivtipm.github.io/Programming/Glava04/index04.htm#z114

__author__ = "Влад Гурбатов"


import source

assert source.find_sum(5) == 1.6228956228956228
assert source.find_sum(100) == 90.71057106928244
assert source.find_sum(32) == 24.98744035464891

s = 0
n = int(input("Введите кол-во итераций: "))
# нахождение результата в цикле
s = source.find_sum(n)
# вывод
print(f"Результат: {s:.4f}")