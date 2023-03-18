__autor__ = "Влад Гурбатов"


def sum_array(a:list):
	"""Вычисление суммы"""
	s = 0
	for i in range(len(a)):
		s += (abs(a[i])**1/2 - a[i])**2
	return s

def create_array(n:int):
	a = []
	for i in range(0, n):
		a.append(int(input("Введите число: ")))
	return a

def print_array(a:list):
    for i in range(len(a)):
            print(f"{a[i]}  ", end='')
    print()