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
from threading import Thread

maiuscula = string.ascii_uppercase
minuscula = string.ascii_lowercase

quant_threads = 2

def gerar_pacientes_aleatorios(fila, tamanho):
    fila = [0] * tamanho

    """
    thread1 = Thread(target=gerar_pacientes_aleatorios_aux, args=[fila, 0, tamanho//4])
    thread2 = Thread(target=gerar_pacientes_aleatorios_aux, args=[fila, tamanho//4, tamanho//2])
    thread3 = Thread(target=gerar_pacientes_aleatorios_aux, args=[fila, tamanho//2, 3*tamanho//4])
    thread4 = Thread(target=gerar_pacientes_aleatorios_aux, args=[fila, 3*tamanho//4, tamanho])

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    """

    thread = [0] * quant_threads
    comeco, fim = 0, tamanho//quant_threads
    intervalo = tamanho//quant_threads
    for i in range(quant_threads):
        if i == quant_threads-1:
            fim = tamanho

        thread[i] = Thread(target=gerar_pacientes_aleatorios_aux, args=[fila, comeco, fim])
        comeco = fim
        fim += intervalo

    for i in range(quant_threads):
        thread[i].start()

    for i in range(quant_threads):
        thread[i].join()

    return fila


def gerar_pacientes_aleatorios_aux(fila, comeco, fim):
    for i in range(comeco, fim):
        nome = ''.join([random.choice(maiuscula)])
        nome += ''.join(random.choice(minuscula) for _ in range(random.randrange(3, 10)))

        sexo = ''.join([random.choice("MF")])

        idade = random.randrange(0, 121)

        gravidade = random.randrange(1, 6)

        fila[i] = Paciente(nome, sexo, idade, gravidade, i+1)


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