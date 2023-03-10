# ввод чисел Даны два действительных положительных числа.
# Найти среднее арифметическое и среднее геометрическое этих чисел.
# https://ivtipm.github.io/Programming/Glava01/index01.htm#z4

__author__ = "Влад Гурбатов"

import os
# запуск должен производить из папки с программой или будет ошибка в поиске модуля
# при в воде абсолютного путя в путь к модулю нужно вводить \\ вместо \ иначе будет ошибка при поиске
p = os.path.abspath('..\\modules ')
print(p)
import sys
sys.path.append(p)
import source


a = float( input("Введите 1 число: ") )
b = float( input("Введите 2 число: ") )
# вычисления по условию
sa = source.sa(a,b)
sg = source.sg(a,b)
assert (2 + 4) / 2 == 3
assert (2 + 6) / 2 == 4
assert (4 + 6) / 2 == 10
# вывод чисел
print(f"Среднее арифметическое {sa:.4f}")
print(f"Среднее геометрическое этих {sg:.4f}")
