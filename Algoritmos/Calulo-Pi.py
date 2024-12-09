'''
- O número π pode ser calculado por meio da série infinita: 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 -1/11 + 1/13 ...)
Elabore um script em Python que calcule e exiba o valor do número π, utilizando a série anterior, 
até que o valor absoluto da diferença entre o número calculado em uma iteração e o da anterior 
seja menor ou igual a 0.00000000005.

Cada termo da sequência tem a seguinte fórmula: (-1)^i * 1/(2*i+1), com i começando em 0, até o além.
Assim que iniciamos uma iteração, o valor da parcela antiga recebe o valor da parcela nova da iteração anterior,
e o valor da parcela nova nessa iteração passa a ser o dado pela fórmula acima.
Em seguida, basta adicionarmos essa parcela na soma total, e guardar o valor absoluto da diferença das parcelas
(em valores absolutos também) e incrementar o valor de i em uma unidade

Jarlisson Moreira, Python Progressivo
'''
sum = 0 
i = 0

parcela_ant = 0
parcela_nov = 0

delta = 1

while(delta > 0.0000000005):
  parcela_ant = parcela_nov
  parcela_nov = pow(-1,i)*1/(2*i + 1)
  sum += parcela_nov
  delta = abs(abs(parcela_ant)-abs(parcela_nov))
  i += 1

print(4*sum)
