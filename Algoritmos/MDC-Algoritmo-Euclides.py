# Neste algoritmo, vamos calcular o MDC (máximo divisor comum) de dois
# números, usando o método de Euclides.

# Para efeitos de comparação, podemos usar também a função gcd() da
# biblioteca 'math', nativa do Python

# Jarlisson Moreira, www.pythonprogressivo.net

import math

x = int(input("Insira o primeiro número: "))
y = int(input("Insira o segundo  número: "))

#print("Resultado da biblioteca math: ", math.gcd(x,y))

print("O MDC entre ",x," e ",y," é: ", end='')
resto = 0
while( y != 0 ):
  resto = x % y
  x = y
  y = resto

print(x)
