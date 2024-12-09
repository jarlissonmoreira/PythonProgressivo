'''
- Crie um programa que recebe um número e verifica se ele é palíndromo ou não.
- Palíndromo é o número que é igual se lido da esquerda pra direita e da direita para a esquerda.

Primeiro, vamos quebrar o número, extraindo sempre o último dígito (com resto da divisão por 10), e o salvando em uma lista.
Após o último dígito, temos que atualizar o número original, subtraindo o dígito retirado e dividindo o restante por 10.

Na lista, vamos comparar o número primeiro com último, o segundo com o penúltimo, o terceiro com o antepenúltimo...
Se N = len(digitos) for o número de dígitos, basta comparar o dígito de índice 0 com o (N-1), o de índice 1 com o (N-1-1),
o de índice 2 com o de índice (N-1-2), até a metade da lista (que é achada com a divisão inteira N//2)

Jarlisson Moreira, www.pythonprogressivo.net
'''

x = int(input("Insira um número inteiro positivo: "))

digitos = []

# Algoritmo para extrair o último digito do numero
# Extrai, salva na lista e modifica o número original
# 1234 -> 123 (salvou 4) -> 12 (salvou 3) -> 1 (salvou 2) -> 0 (salvou 1, parou em 0)
while(x>0):
  ultimo = int(x%10)
  digitos.append(ultimo)

  x = x - ultimo
  x = x/10

# Verificando se o numero de índice [i] é igual ao de [N-i-1]
# se não for, não é palíndromo e alteramos o booleano abaixo
is_palin = True

for i in range(len(digitos)//2):
  if digitos[i] != digitos[len(digitos)-i-1]:
    is_palin = False
    break
    
if is_palin:
  print("Palindromo")
else:
  print("Nao é palindromo")
