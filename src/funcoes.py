import os
import random
import string
import time
import matplotlib
import matplotlib.pyplot as plt
from paciente import Paciente
from ordenacoes import *
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import multiprocessing as mp
from graphviz import Graph

maiuscula = string.ascii_uppercase
minuscula = string.ascii_lowercase
potencia_maxima = 17
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
    heap_sort_recursivo(fila)
    fim = time.perf_counter()
    lista_tempos['HSR'] = (fim - inicio)

    # Heap Sort Interativo - HSI
    fila = desordenado.copy()
    inicio = time.perf_counter()
    heap_sort_interativo(fila)
    fim = time.perf_counter()
    lista_tempos['HSI'] = (fim - inicio)

    tipos = ['Heap Sort Recursivo', 'Heap Sort Interativo']
    tempos = [lista_tempos['HSR'], lista_tempos['HSI']]

    _, ax = plt.subplots(figsize=(16, 9))
    ax.set(xlabel='Metodo de Ordenacao', ylabel='Tempo (s)')
    plt.figure(1)
    plt.bar(tipos, tempos)

    for i, v in enumerate(tempos):
        plt.text(i-0.1, max(tempos)/100, " "+str(v), color='black',
                 va='center', fontweight='bold', fontsize=12)

    plt.suptitle('Tempo em segundos para ordenar {} pacientes'.format(len(fila)))
    plt.show()


def calc_tempos_HSR(fila, tempos):
    vetor_swaps = []
    vetor_heap = []
    for i in range(potencia_maxima):
        inicio = time.perf_counter()
        swaps, heapify = heap_sort_recursivo(fila[i])
        fim = time.perf_counter()
        vetor_swaps.append(swaps)
        vetor_heap.append(heapify)
        tempos.append(fim-inicio)
        
    return vetor_heap, vetor_swaps

def calc_tempos_HSI(fila, tempos):
    vetor_swaps = []
    for i in range(potencia_maxima):
        inicio = time.perf_counter()
        swaps = heap_sort_interativo(fila[i])
        fim = time.perf_counter()
        vetor_swaps.append(swaps)
        tempos.append(fim-inicio)

    return vetor_swaps

def comparacoes():
    desordenado = []
    fila_HSR = []
    fila_HSI = []
    tempo_HSR = []
    tempo_HSI = []

    for i in range(potencia_maxima):
        fila_HSR.append([])
        fila_HSI.append([])
    
    for i in range(potencia_maxima):
        desordenado = gerar_pacientes_aleatorios(2**(i+1))
        fila_HSR[i] = desordenado.copy()
        fila_HSI[i] = desordenado.copy()

    heapHSR, swapsHSR = calc_tempos_HSR(fila_HSR, tempo_HSR)
    swapsHSI = calc_tempos_HSI(fila_HSI, tempo_HSI)

    
    printar_grafico(tempo_HSR, tempo_HSI, swapsHSR, heapHSR, swapsHSI)

def printar_grafico(HSR, HSI, swapsHSR, heapHSR, swapsHSI):
    printar_swaps(swapsHSR, heapHSR, swapsHSI)
    x = np.array([])

    for i in range(potencia_maxima):
        z = 2**(i+1)
        x = np.append(x, z)

    t = x

    fig, ax = plt.subplots()
    ax.set_title('Comparação entre os Algoritmos')
    ax.set(xlabel='Quantidade de elementos', ylabel='Tempo (s)')
    line1, = ax.plot(t, HSR, lw=2, color='red', label='Heap Sort Recursivo')
    line2, = ax.plot(t, HSI, lw=2, color='blue', label='Heap Sort Interativo')
    leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
    leg.get_frame().set_alpha(0.4)

    lines = [line1, line2]
    lined = dict()
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(2)
        lined[legline] = origline


    def onpick(event):
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)

        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', onpick)

    plt.show()

def printar_swaps(swapsHSR, heap, swapsHSI):
    x = np.array([])

    for i in range(potencia_maxima):
        z = 2**(i+1)
        x = np.append(x, z)

    t = x

    fig, ax = plt.subplots()
    ax.set_title('Comparação entre os Algoritmos')
    ax.set(xlabel='Quantidade de elementos ordenados', ylabel='Quantidade de Swaps e Heapify')
    line1, = ax.plot(t, swapsHSR, lw=2, color='red', label='Swaps Heap Sort Recursivo')
    line2, = ax.plot(t, heap, lw=2, color='blue', label='Heapify Heap Sort Recursivo')
    line3, = ax.plot(t, swapsHSI, lw=2, color='green', label='Swaps Heap Sort Iterativo')
    leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
    leg.get_frame().set_alpha(0.4)

    lines = [line1, line2, line3]
    lined = dict()
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(2)
        lined[legline] = origline


    def onpick(event):
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)

        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', onpick)



def printar_arvore(v):
    dic_num_color = {5: 'red', 4: 'orange', 3: 'yellow', 2: 'green', 1: 'dodgerblue'}
    n = len(v)
    if n == 0:
        return
    
    dot = Graph(format='png')
    for i in range(n):
        dot.node(v[i].nome, fillcolor=dic_num_color[v[i].gravidade], style='filled')

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            dot.edge(v[i].nome, v[left].nome, constraint='true')
        
        if right < n:
            dot.edge(v[i].nome, v[right].nome, constraint='true')

    dot.render('fila.gv', view=True)