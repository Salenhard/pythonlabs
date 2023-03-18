

__autor__ = "Влад Гурбатов"

import math 
import matplotlib.pyplot as plt
import numpy as np 
# np.arange создаёт массив от start до stop элементов с указаным шагом step
x = np.arange(0,100,0.1)
# создаёт лист из элементов x**2
y = np.cos(x) * x
y1 = y + np.random.uniform(-10,10,1000)
# название графика
plt.title("Пример")
# подпись x оси
plt.xlabel("x")
# подпись y оси
plt.ylabel("y")
# вывод графика с задаными координатами и навзанием cos(x)*x
plt.plot(x,y, label = 'cos(x)*x')
# вывод графика с задаными координатами и навзанием noise alpha - прозрачность графика
plt.plot(x, y1, label = 'noise', alpha = 0.5)
# вывод сетки на экран
plt.grid(True)
# вывод названий графиков
plt.legend()
plt.show()
