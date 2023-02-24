#Определить, является ли данное целое число четным.
#https://ivtipm.github.io/Programming/Glava03/index03.htm#z62
__autor__ = "Влад Гурбатов"

import source

# Ввод числа
a = int(input("Введите число для проверки"))
# проверка числа на чётность
assert 2 % 2 == 0
if source.is_even(a):
    print("Чётное")
e: print("Не чётное")