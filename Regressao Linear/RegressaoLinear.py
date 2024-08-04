# Regressão Linear usando o Método dos mínimos quadrados
# Curso Python Progressivo / Programação Científica com Python
# @author: Jarlisson Moreira, jarlisson.moreira @ gmail com
# tutorial: https://www.pythonprogressivo.net/2024/08/Regressao-Linear-Metodo-Minimos-Quadrados-Python.html

import numpy as np
import matplotlib.pyplot as plt

# Massas(em gramas) e respectivas Distensões da mola deltax (em centímetros)
massa = np.array([10.7, 20.6, 30.8, 41.1, 50.9, 60.8, 71.2])
delta_x = np.array([6.4, 8.0, 8.8, 10.0, 11.0, 12.8, 13.5])

#Comprimentos totais da mola
L0 = 5.0
L = L0 + delta_x

# Seja: l = l0 + Bm a equação da reta que relaciona o tamanho
# final da mola (l), com seu tamanho inicial (l0) e o valor da massa (m)
# B representa a constante g/k (onde g é a acelaração da gravidade) e k
# a constante da mola

## Regressão linear: y = A + Bx
# x é a massa e y é o l

# Número de experimentos
N = 7

# Somatório de x[i] (massas)
S_m = massa.sum()

# Somatório de l[i] (comprimentos)
S_l = L.sum()

# Somatório dos quadrados x²[i] das massas
S_m2 = sum(i*i for i in massa)

# Somatório dos quadrados dos comprimentos l²[i]
S_l2 = sum(i*i for i in L)

# Somatório dos produtos de cada massa pelo seu respectivo comprimento final m[i]*l[i]
S_ml = 0.0
for i in range(N):
  S_ml = S_ml + massa[i]*L[i]

# Colocando tudo na fórmula
delta = N*S_m2 - (S_m*S_m)
A = ((S_m2 * S_l) - S_m * S_ml)/(delta)
B = ((N*S_ml) - S_m * S_l)/(delta)

# Reta com os novos valores, Yi
y = np.array(A + B*massa)

# Incerteza de y, A e B, com uma unidade de incerteza
residuo=0.0
y=y.round(1)
A=round(A,1)
B=round(B,1)

for i in range(N):
  residuo = residuo + np.power(y[i] - A - B*massa[i], 2)

dy = round(np.sqrt(residuo/(N-2)),1)
dA = round(dy * np.sqrt(S_m2/delta),1)
dB = round(dy * np.sqrt(N/delta),1)

# B e seu erro dB estão em centimetros/gramas = 10 metros/kilogramas
B_kgm = B*10.0
dB_kgm = dB*10.0

# Constante da mola, e seu erro propagado de B
# pois B = g/k
K = 9.8/B_kgm
dK = dB_kgm * ( 9.8/(B_kgm*B_kgm) )

# Gerando o gráfico
fig, ax = plt.subplots()
fig.suptitle('Massa(g) x Tamanho da mola (cm)')
plt.rcParams.update({'font.size': 12})

ax.title.set_text('Curso Python Progressivo')
ax.scatter(massa, L, marker='.', s=1)
ax.plot(massa, y, color='red', linestyle='--', label='reta mmq')
ax.errorbar(massa, L, yerr=dy, fmt='.k', label='dados experimentais')
ax.legend(loc="lower right")
plt.show()

## Visualizando os dados, para controle e checagem
print("Somatorio das massas: ", S_m)
print("Somatorio quadrado das massas: ", S_m2)
print("Somatorio comprimento: ", S_l)
print("Somatorio quadrado do scomprimentos: ", S_l2)
print("Somatorio massa pelo comprimento menores: ", S_ml)
print("Delta: ", delta)
print("A: %.2f cm"% A)
print("B: %.2f cm/g"% B)
print("Reta da mola: y = %.1f + %.1f*m" % (A, B))
print("Erro y: ", dy)
print("Erro A: ", dA)
print("Erro B: ", dB)
print("Constante: ", K)
print("Erro de k: ", dK)
print("K = %.1f +- %.1f" %(K, dK))
