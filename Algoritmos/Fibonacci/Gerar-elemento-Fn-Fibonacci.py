'''
- Crie um script em Python que gera o n-ésimo termo da sequência de Fibonacci, onde os dois primeiros termos são:
f0 = 0 e f1 = 1, e o termo seguinte é sempre a soma dos dois termos anteriores

Jarlisson Moreira, www.pythonprogressivo.net
'''
N = int(input("Insira um número inteiro positivo maior que 2: "))

f0 = 0
f1 = 1

for i in range(3,N+1):
  # Próximo termo
  f2 = f1 + f0

  # Atualizando os novos valores de f0 e f1
  # para a próxima iteração
  temp = f1
  f1 = f2
  f0 = temp

print(f2)

