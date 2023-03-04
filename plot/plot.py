

__autor__ = "Влад Гурбатов"


import matplotlib.pyplot as plt
import numpy as np 

x = np.random.randint(0, 100 ,100)
y = list(map(x:**2, y))
plt.plot(x,y)
plt.show()
