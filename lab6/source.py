__autor__ = "Влад Гурбатов"


def print_massive(a:list, n:int):
    for i in range(0, n):
        print(a[i], " ", end='')
    print()


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