# Script para plotar um gráfico do tipo Histograma, em Python
# Curso Python Progressivo / Programação Científica com Python
# @author: Jarlisson Moreira, jarlisson.moreira @ gmail com
# tutorial: https://www.pythonprogressivo.net/2024/08/Como-plotar-grafico-Histograma-Python.html

import numpy as np
from matplotlib import pyplot

def plot_histograma(path: str = None, data: str = None, bins: float | str = None) -> None:
    #path: caminho do arquivo .txt com os dados "caminho/do/data.txt"
    #bins: se nao fornecido retorna o histograma dos valores individuais,
    #ele pode ser tamanho (float), ou uma string com valores: 'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', or 'sqrt'
    #return: printa na tela o histograma
    
    if path is not None:
        with open(path, "r") as file:
            content = file.read().replace(',', '.')
            values: list[float] = [float(i) for i in content.split()]
    else:
        content = data.replace(',', '.')
        values: list[float] = [float(i) for i in content.split(';')]
   
    array = np.array(values)
    
    if bins is None:
        bins=sorted(values)
       
    if type(bins) is str:
        bins=bins
       
    if type(bins) is float:
        bins = np.arange(array.min(), array.max() + bins, bins)
    
    #Transforma o array/lista de valores em uma matriz com 10 colunas
    col = 10
    lin = int(len(array)/col)
    array2 = array.reshape(lin,col)
    
    #Cria um array, onde cada elemento é uma média de 10 valores,
    #de cada linha da matriz anterior
    median=np.mean(array2, axis=1)
    
    #Novo código para imprimir os três gráficos, com mesmo eixo x
    fig, (ax1, ax2, ax3) = pyplot.subplots(3, 1, sharex=True)

    #Primeiro gráfico, de 1350 medições
    ax1.hist(array, bins)
    ax1.xaxis.set_tick_params(labelbottom=True)
    leg1 = str(lin*col)
    ax1.set_xlabel(leg1+' medições')

    #Segundo gráfico, das 135 médias
    ax2.hist(median,bins)
    ax2.xaxis.set_tick_params(labelbottom=True)
    leg2 = str(len(median))
    ax2.set_xlabel(leg2+' médias')
    
    #Sobrepondo os dois, para efeitos de comparação
    ax3.hist(array, bins, alpha=0.5, label=leg1)
    ax3.hist(median, bins, alpha=0.5, label=leg2)
    ax3.set_xlabel('Gráficos sobrepostos')
    ax3.legend(loc='upper right')
    
    pyplot.tight_layout()
    pyplot.show()

path="data.txt"
data=None
bins='auto'
plot_histograma(path,data,bins)
