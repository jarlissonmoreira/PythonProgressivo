# Regressão Linear usando a função linregress() da biblioteca SciPy
# Curso Python Progressivo / Programação Científica com Python
# @author: Jarlisson Moreira, jarlisson.moreira @ gmail com
# tutorial: https://www.pythonprogressivo.net/2024/08/Regressao-Linear-Metodo-Minimos-Quadrados-Python.html

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def func(x):
  return result.slope * x + result.intercept

# Massas(gramas) e respectivas Distensões da mola (centímetros)
massa = np.array([10.7, 20.6, 30.8, 41.1, 50.9, 60.8, 71.2])
delta_x = np.array([6.4, 8.0, 8.8, 10.0, 11.0, 12.8, 13.5])

# Comprimento total da mola
L0=5.0
L = np.array(L0 + delta_x)

# Armazenando os parametros
# Retorna a tupla com: B(coefieciente angular da reta), intercept (A, onde toca o eixo x), 
# rvalue (coeficiente Pearson de correlação), pvalue (valor-p da probabilidade), 
# stderr (erro padrão do parâmetro slope), intercept_stderr (erro padrão do parâmetro intercept)
result = stats.linregress(massa, L)

modelo = list(map(func, massa))

# Gerando o gráfico
fig, ax = plt.subplots()
fig.suptitle('Massa(g) x Tamanho da mola (cm), com SciPy')
plt.rcParams.update({'font.size': 12})
ax.title.set_text('Curso Python Progressivo')
ax.scatter(massa, L, marker='.')
ax.plot(massa, modelo, color='red', linestyle='--', label='reta mmq')
plt.show()

## Imprimindo os dados
print("B (coeficiente angular): ",result.slope)
print("A (onde incercepta o eixo x): ", result.intercept)
print("rvalue : ", result.rvalue)
print("pvalue : ", result.pvalue)
print("stderr (erro padrão do slope, B): ", result.stderr)
print("intercept_stderr (erro padrão do incercept, A): ",result.intercept_stderr)
