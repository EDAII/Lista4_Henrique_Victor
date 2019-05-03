qtd_heapify = 0
swaps = 0
def heapify(v, n, i):
    menor = i           # Inicializa menor como raiz
    left = 2 * i + 1
    right = 2 * i + 2 

    # Veririfca se o filho da esquerda da raiz existe e
    # se é menor que a raíz
    if left < n and v[i] > v[left]: 
        menor = left 

    # Veririfca se o filho da direita da raiz existe e
    # se é menor que a raíz
    if right < n and v[menor] > v[right]: 
        menor = right 

    global swaps
    # Muda a raíz, se necessário
    if menor != i:
        swaps += 1
        v[i], v[menor] = v[menor], v[i]
 
        # Dá um Heapify na raíz
        global qtd_heapify
        qtd_heapify += 1
        heapify(v, n, menor)


def heap_sort_recursivo(v):
    global qtd_heapify
    global swaps
    qtd_heapify = 0
    swaps = 0

    n = len(v)
    # Constrói um Min Heap
    for i in range(n, -1, -1): 
        heapify(v, n, i)

    for i in range(n-1, 0, -1):
        swaps += 1
        v[i], v[0] = v[0], v[i]
        heapify(v, i, 0)

    #print("Quantidade de Swaps: ", swaps)
    #print("Quantidade de entradas no Heapify: ", qtd_heapify)


def buildMinHeap(v, n):
    global swaps
    for i in range(n): 
        if v[i] < v[int((i - 1) / 2)]: 
            j = i  
 
            while v[j] < v[int((j - 1) / 2)]:
                k = int((j - 1) / 2)
                swaps += 1
                (v[j], v[k]) = (v[k], v[j]) 
                j = k
                if j == 0:
                    break


def heap_sort_interativo(v):  
    global swaps
    swaps = 0
    n = len(v)
    buildMinHeap(v, n)  
  
    for i in range(n - 1, 0, -1): 
        swaps += 1
        v[0], v[i] = v[i], v[0] 
        j, index = 0, 0
          
        while True: 
            index = 2 * j + 1

            if (index < (i - 1) and v[index] > v[index + 1]):  
                index += 1
 
            if index < i and v[j] > v[index]: 
                swaps += 1
                v[j], v[index] = v[index], v[j]  
          
            j = index  
            if index >= i: 
                break
    
    #print("Quantidade de swaps: ", swaps)