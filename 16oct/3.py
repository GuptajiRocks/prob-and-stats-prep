import numpy as np
import matplotlib.pyplot as plt
averg = 7
stddev = 8
n = 9000

sample = np.random.normal(averg, stddev, n)

jesus = np.log(sample[sample>0])
plt.hist(jesus, edgecolor="black")
plt.show()
