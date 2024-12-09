'''
- Crie um script em Python que mostra todos os números triangulares entre 0 e N, N inteiro positivo fornecido pelo usuário.
Vamos usar o código do Numeros-Triangulares.py

Jarlisson Moreira, Python Progressivo
'''

N = int(input("Insira um número inteiro positivo: "))

for n in range(N+1):
  for i in range(n):
    if ( i*(i+1)*(i+2) == n ):
      print(i*(i+1)*(i+2)," = ",i,"*",i+1,"*",i+2)
