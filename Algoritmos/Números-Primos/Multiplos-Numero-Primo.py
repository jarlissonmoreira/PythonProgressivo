'''
- Crie um programa em Python que recebe um número inteiro e em seguida exibe uma lista de todos os seus múltiplos. Verifique, ao final, se ele é primo ou não.
Pedimos um número inteiro ao usuário, depois criamos uma lista inicialmente vazia, para armazenar seus múltiplos.
Depois, fazemos um looping percorrer todos os números, de 1 até o número, verificando o resto da divisão.
Se for múltiplo, adicionamos a lista.
Para saber se é primo, basta verificar se o tamanho da lista é 2 (1 e ele mesmo são os únicos múltiplos).

Jarlisson Moreira, www.pythonprogressivo.net
'''
import math

x = int(input("Insira um número maior que 2: "))

multiplos = []

for i in range(1,x+1):
  if( x % i == 0):
    multiplos.append(i)

print("Lista de múltiplos: ", multiplos)

if(len(multiplos)==2):
  print("É primo.")
else:
  print("Não é primo.")
