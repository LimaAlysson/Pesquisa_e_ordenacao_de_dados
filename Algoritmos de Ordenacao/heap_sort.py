# Aŕvore binária: Os filhos sõa menores que o pai; a árvore é a mais completa possível (completa sempre horizontalmente antes)
# pode ser representada por um vetor
# Complexidade O(nlogn) em todos os casos

def parent(i):
    return (i -1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(lista, i, heap_size):
    l = left(i)
    r = right(i)

    if l < heap_size and lista[l] > lista[i]:
        maior = l
    else:
        maior = i
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        max_heapify(lista, maior, heap_size)


def build_max_heap(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(lista, i, n)


def heapsort(lista):
    build_max_heap(lista)

    n = len(lista)
    heap_size = n

    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heap_size -= 1
        max_heapify(lista, 0, heap_size)