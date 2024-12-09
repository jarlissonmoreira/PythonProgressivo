'''
- Crie um script em Python que receba um número e forneça seu palíndrome: ou seja, o número na ordem contrária dos dígitos.

Jarlisson Moreira, Python Progressivo
'''

N = int(input("Insira um número: "))
p = 0

while(N):
  # Extraindo o último dígito do número digitado
  ultimo = N%10

  # Adicionando o dígito extraído no palíndromo
  p = p*10 + ultimo

  # Retirando o último dígito do número original
  N = N//10

print(p)
