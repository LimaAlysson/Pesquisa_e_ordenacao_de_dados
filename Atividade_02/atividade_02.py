# Equipe:
# Alysson José
# André Igor
# Leonardo Lucena


import random

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    
    if inicio < fim:
        p = particao(lista, inicio, fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)
    
    return lista


def particao(lista, inicio, fim):
    indice_aleatorio = random.randint(inicio, fim)
    pivot = lista[indice_aleatorio]
    #print(pivot)
    lista[indice_aleatorio], lista[fim] = lista[fim], lista[indice_aleatorio]

    i = inicio
    
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]

    return i 


if __name__ == '__main__':
    lista = random.sample(range(0, 100), 10)
    print(lista)
    print('LISTA ORDENADA')
    print(quick_sort(lista))