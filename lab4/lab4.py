#Вычислить:
# i**2/(i**2 + 2*i + 3)
#https://ivtipm.github.io/Programming/Glava04/index04.htm#z114

import source
__autor__ = "Влад Гурбатов"


s = 0
n = int(input("Введите кол-во итераций: "))
# нахождение результата в цикле
assert source.find_sum(n) == 0.363636364
s = source.find_sum(n)
# вывод
print(f"Результат: {s:.4f}")