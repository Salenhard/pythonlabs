

__autor__ = "Влад Гурбатов"


import matplotlib.pyplot as plt
import numpy as np 
import seaborn
# uniform значения действительных чисел из равномерного распределния все значения
# от low до high имеют одинаковый шанс выпадения
a = np.random.uniform( low = 0, high = 100, size = (100) )
#plt.xlabel("")
#plt.hist(a)
seaborn.histplot(a)
plt.show()

