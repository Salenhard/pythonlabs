__author__ = "Гурбатов Владислав"


import seaborn as sb
import numpy as np 
import matplotlib.pyplot as plt
# создание рандомных данные для занесение в heatmap
a = np.random.randint( 0, 10, size=(7,7) )
# создание heatmap на основе данных a cmap - вид heatmap представляет собой температуру
# annot - выводит значения яйчеек матрицы
sb.heatmap(a, cmap="coolwarm", annot = True)
# plt.show средство для вывода графика
plt.show()
