import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt("itub.txt", float)

x = dados[:, 0]
y = dados[:, 1]

plt.plot(x,y)
