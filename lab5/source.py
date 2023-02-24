def array_sum(a:list, n:int):
	"""Вычисление суммы"""
	s = 0
	for i in range(0, n):
		s += abs(a[i])**1/2 - a[i]
	return s
def create_array(n:int):
	a = []
	for i in range(0, n):
		a.append(int(input("Введите число: ")))
	return a
