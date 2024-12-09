'''
- Escreva um programa que exibe todos os números primos entre 1 e N, com N um inteiro positivo fornecido pelo usuário.
Vamos usar a função prime(x) para verificar se x é primo ou não (ver Primo.py).
Faremos um looping percorrendo o intervalo 2 até (x-1), e testando se cada um desses valores é primo

Jarlisson Moreira, www.pythonprogressivo.net
'''

def prime(x):
  is_prime = True

  for i in range(2,x):
    if( x % i == 0):
      is_prime = False

  return is_prime

x = int(input("Insira um número inteiro positivo: "))

primos = []

for i in range(2,x):
  if( prime(i) == True):
    primos.append(i)

print("Primos existentes entre 1 e ",x,": ", primos)
