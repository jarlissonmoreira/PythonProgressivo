import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt("densidade.txt",float)
plt.imshow(dados)
plt.show()
