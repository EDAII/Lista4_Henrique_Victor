import os
import random
import string
import time
import matplotlib
import matplotlib.pyplot as plt
from paciente import Paciente
from ordenacoes import *
import plotly
import plotly.graph_objs as go
import numpy as np
import multiprocessing as mp

maiuscula = string.ascii_uppercase
minuscula = string.ascii_lowercase
output = mp.Queue()

quant_process = 8

def gerar_pacientes_aleatorios(tamanho):
    pool = mp.Pool(processes=quant_process)
    fila = pool.map(gerar_pacientes_aleatorios_aux, range(0, tamanho))

    return fila


def gerar_pacientes_aleatorios_aux(i):
    nome = ''.join([random.choice(maiuscula)])
    nome += ''.join(random.choice(minuscula) for _ in range(random.randrange(3, 10)))

    sexo = ''.join([random.choice("MF")])

    idade = random.randrange(0, 121)

    gravidade = random.randrange(1, 6)

    return Paciente(nome, sexo, idade, gravidade, i+1)

def paciente_unico(fila, nome, sexo, idade, gravidade):
    fila.append(Paciente(nome, sexo, idade, gravidade, len(fila) + 1))


def mostrar_fila(fila, tamanho):
    nomes = []
    sexos = []
    idades = []
    gravidades = []
    ordemChegadas = []

    for i in range(tamanho):
        nomes.append(fila[i].nome)
        sexos.append(fila[i].sexo)
        idades.append(fila[i].idade)
        gravidades.append(fila[i].gravidade)
        ordemChegadas.append(fila[i].ordemChegada)

    indices = ['<b>NOMES</b>', '<b>SEXOS</b>', '<b>IDADES</b>',
               '<b>GRAVIDADE</b>', '<b>ORDEM DE CHEGADA</b>']
    trace = go.Table(
        header=dict(
            values=indices,
            line=dict(color='#000'),
            fill=dict(color='blue'),
            font=dict(color='#fff', size=20)
        ),
        cells=dict(
            values=[nomes, sexos, idades, gravidades, ordemChegadas],
            font=dict(color='#000', size=14),
            fill=dict(color='#F1F8FB'),
            height=25
        )
    )

    data = [trace]
    plotly.offline.plot(data, filename='fila.html')


def comparar_ordenacoes(fila, desordenado):
    lista_tempos = {}

    # Heap Sort Recursivo - HSR
    fila = desordenado.copy()
    inicio = time.perf_counter()
    merge_sort(fila)
    fim = time.perf_counter()
    lista_tempos['HSR'] = (fim - inicio)

    # Heap Sort Interativo - HSI
    fila = desordenado.copy()
    inicio = time.perf_counter()
    merge_sort(fila)
    fim = time.perf_counter()
    lista_tempos['HSI'] = (fim - inicio)

    tipos = ['Heap Sort Recursivo', 'Heap Sort Interativo']
    tempos = [lista_tempos['HSR'], lista_tempos['HSI']]

    _, ax = plt.subplots(figsize=(16, 9))
    ax.set(xlabel='Metodo de Ordenacao', ylabel='Tempo (s)')
    plt.figure(1)
    plt.bar(tipos, tempos)

    for i, v in enumerate(tempos):
        plt.text(i-0.4, max(tempos)/100, " "+str(v), color='black',
                 va='center', fontweight='bold', fontsize=12)

    plt.suptitle(
        'Tempo em segundos para ordenar {} pacientes'.format(len(registros)))
    plt.show()


def comparacoes():
    pass

def printar_grafico():
    pass