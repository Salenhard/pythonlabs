__author__ = "Гурбатов Владислав"


import seaborn as sb
import numpy as np 
import matplotlib.pyplot as plt
# создание рандомных данные для занесение в heatmap
a = np.random.randint( 0, 10, size=(30,30) )
# создание heatmap на основе данных a cmap - вид heatmap представляет собой температуру
sb.heatmap(a, cmap="coolwarm")
# plt.show средство для вывода графика
plt.show()
