# Даны три действительных числа. Выбрать из них те, которые принадлежат интервалу (1, 3).
# https://ivtipm.github.io/Programming/Glava02/index02.htm#z41
# ввод чисел в массив

import source

__autor__ = "Влад Гурбатов"


# input.split - разделяет введённые числа в массив,  map() — это встроенная функция, которая позволяет обрабатывать и преобразовывать все элементы, list - переводит значения в лист
a = list(map(int, input("Введите чило: ").split() ))
print("Числа в диапозоне 0 < x < 4:\n")
for i in range(3):
    if source.diaposon(0,3,a[i]):
        print(a[i])
assert 0 < 2 < 3