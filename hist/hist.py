

__autor__ = "Влад Гурбатов"


import matplotlib.pyplot as plt
import numpy as np 


a = np.random.uniform( low = 0, high = 100, size = (100) )
plt.hist(a)
plt.show()

