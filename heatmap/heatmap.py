__author__ = "Гурбатов Владислав"


import seaborn as sb
import numpy as np 
import matplotlib.pyplot as plt


a = np.random.randint( 0, 10, size=(30,30) )
sb.heatmap(a, cmap="coolwarm");
plt.show()
