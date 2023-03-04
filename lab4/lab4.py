#Вычислить:
# i**2/(i**2 + 2*i + 3)
#https://ivtipm.github.io/Programming/Glava04/index04.htm#z114

__author__ = "Влад Гурбатов"


import source



s = 0
n = int(input("Введите кол-во итераций: "))
# нахождение результата в цикле
assert source.find_sum(5) == 0.363636364
s = source.find_sum(n)
# вывод
print(f"Результат: {s:.4f}")