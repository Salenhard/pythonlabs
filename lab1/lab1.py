# ввод чисел Даны два действительных положительных числа.
# Найти среднее арифметическое и среднее геометрическое этих чисел.
# https://ivtipm.github.io/Programming/Glava01/index01.htm#z4

__autor__ = "Влад Гурбатов"

import source


a = float( input("Введите 1 число: ") )
b = float( input("Введите 2 число: ") )
# вычисления по условию
sa = source.sa(a,b)
sg = source.sg(a,b)
assert (2 + 4) / 2 == 3
# вывод чисел
print(f"Среднее арифметическое {sa:.4f}")
print(f"Среднее геометрическое этих {sg:.4f}")
