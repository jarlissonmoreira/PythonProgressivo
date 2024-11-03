import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt("estrelas.txt", float)
x = dados[:, 0]
y = dados[:, 1]

plt.xlim(0, 14000)
plt.ylim(-3, 20)
plt.xlabel("Temperatura")
plt.ylabel("Brilho")
plt.scatter(x,y, s=10)
plt.show()
