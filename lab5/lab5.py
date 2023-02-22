#Даны натуральное число n, действительные числа a1,..., an. Вычислить:
#(sqrt(ai)-ai)**2 
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136



__author__ = "Влад Гурбатов"


def array_sum(a:list, n:int):
	"""Вычисление суммы"""
	s = 0
	for i in range(0, n):
		s += abs(a[i])**1/2 - a[i]
	return s


# ввод размера массива
n = int(input("Введите размер массив: "))
a = [] 
for i in range(0, n):
	a.append(int(input("Введите число: ")))
print(f"Результат: {array_sum(a,n):.4f}")
