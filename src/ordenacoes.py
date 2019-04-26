def heapify(v, n, i): 
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and v[i] > v[l]: 
        largest = l 

    if r < n and v[largest] > v[r]: 
        largest = r 

    if largest != i: 
        v[i], v[largest] = v[largest], v[i]
 
        heapify(v, n, largest)


def heap_sort_recursivo(v): 
    n = len(v) 

    for i in range(n, -1, -1): 
        heapify(v, n, i)

    for i in range(n-1, 0, -1): 
        v[i], v[0] = v[0], v[i]
        heapify(v, i, 0)


def buildMaxHeap(v, n):  
    for i in range(n): 
        if v[i] < v[int((i - 1) / 2)]: 
            j = i  
 
            while v[j] < v[int((j - 1) / 2)]:
                k = int((j - 1) / 2)
                (v[j], v[k]) = (v[k], v[j]) 
                j = k


def heap_sort_interativo(v):  
    n = len(v)
    buildMaxHeap(v, n)  
  
    for i in range(n - 1, 0, -1):  
        v[0], v[i] = v[i], v[0] 
        j, index = 0, 0
          
        while True: 
            index = 2 * j + 1

            if (index < (i - 1) and v[index] > v[index + 1]):  
                index += 1
 
            if index < i and v[j] > v[index]:  
                v[j], v[index] = v[index], v[j]  
          
            j = index  
            if index >= i: 
                break