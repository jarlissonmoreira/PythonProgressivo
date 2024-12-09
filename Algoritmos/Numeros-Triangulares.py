'''
- Crie um programa em Python que recebe um número inteiro positivo e diz se ele é triangular ou não.
- Um número triângulo N é aquele que é da forma: N = n*(n+1)*(n+2)
- Por exemplo, 210 é triangular, pois: 210 = 5 * 6 * 7

Vamos fazer um looping percorrer dos números 0 até N-2, pois neste último caso vamos testar:
(N-2)*(N-1)*N 
Se encontrar uma sequência que torna N é triangular, ele imprime e termina o looping.
Se chegar na última iteração, printa que não é triangular

Jarlisson Moreira, Python Progressivo
'''

n = int(input("Insira um número inteiro positivo: "))

for i in range(n):
    if ( i*(i+1)*(i+2) == n ):
      print("É triangular: ",i,"*",i+1,"*",i+2," = ",i*(i+1)*(i+2))
      break
    if i==n-1:
      print("Não é triangular")
