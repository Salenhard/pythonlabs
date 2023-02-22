# Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:
# удовлетворяющих условию a[k] < (a[k-1] - a[k+1])/2
# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178


 
__author__ = "Влад Гурбатов"


def print_massive(a:list):
	for i in a:
		print(f"{i}: {a[i]:.4f}")


def array_filter(a:list, n:int):
	b = []
	for k in range(1, n-1):
		if a[k] < ((a[k-1] - a[k+1]) / 2):
			b.append(a[k])
	"""Поиск элемента соотвествующего условию"""
	return b


def create_mas(n:int):
	"""Функция создания массива размером n"""
	a = []
	for i in range(0, n):
		a.append(int(input("Введите число: ")))
	return a


# ввод значений
n = int(input("Введите размер массива: "))
a = create_mas(n)

print("Результат: ", print_massive(array_filter(a,n)))
