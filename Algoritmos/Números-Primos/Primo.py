'''
- Crie um programa em Python que verifica se um número é primo ou não.

O código abaixo verifica se um número maior que 2 é primo ou não
Jarlisson Moreira, www.pythonprogressivo.net
'''
x = int(input("Insira um número maior que 2: "))

is_prime = True

for i in range(2,x):
  if( x % i == 0):
    is_prime = False

if is_prime:
  print(x, "é primo.")
else:
  print(x, "não é primo.")
