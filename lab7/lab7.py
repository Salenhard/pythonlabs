# Вычислить:
# i0->100 j0->100:(j-i+1)/(i+j)
# https://ivtipm.github.io/Programming/Glava10/index10.htm#z334


__author__ = "Гурбатов Владислав"
n = int(input("Введите кол-во итераций в 1 цикле: "))
m = int(input("Введите кол-во итераций во 2 цикле: "))
s = 0
# цикл
for i in range(1, n):
	for j in range(1, m):
			s += (j-i+1)/(i+j)
print(f"Результат: {s:.4f}")