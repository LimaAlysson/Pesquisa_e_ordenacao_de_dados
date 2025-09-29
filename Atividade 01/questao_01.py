import random

def bubble_sort(lista):

    n = len(lista)

    for _ in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def selection_sort(lista):

    n = len(lista)

    for j in range(n-1):
        min = j
        for i in range(j, n):
            if lista[i] < lista[min]:
                min = i
    
    if lista[j] > lista[min]:
        lista[j], lista[min] = lista[min], lista[j]
    
    return lista

def insertion_sort(lista):

    n = len(lista)

    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j > -1 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave

    return lista

if __name__ == '__main__':
    lista = random.sample(range(1, 100), 10)
    print("\n*** LISTA DESORDENADA ***")
    print(lista)
    print("\n*** BUBBLE SORT ***")
    print(bubble_sort(lista))
    print("\n*** SELECTION SORT ***")
    print(selection_sort(lista))
    print("\n*** INSERTION SORT ***")
    print(insertion_sort(lista))


# Equipe: Alysson José, André Igor, Leonardo Lucena