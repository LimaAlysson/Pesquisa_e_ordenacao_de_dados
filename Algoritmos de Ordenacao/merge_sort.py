# Complexidade O(nlogn) em todos os casos


def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if(fim - inicio > 1):
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    
    return lista

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    menor_esquerda, menor_direita = 0, 0

    for i in range(inicio, fim):
        if menor_esquerda >= len(esquerda):
            lista[i] = direita[menor_direita]
            menor_direita += 1
        elif menor_direita >= len(direita):
            lista[i] = esquerda[menor_esquerda]
            menor_esquerda += 1
        elif esquerda[menor_esquerda] < direita[menor_direita]:
            lista[i] = esquerda[menor_esquerda]
            menor_esquerda += 1
        else:
            lista[i] = direita[menor_direita]
            menor_direita += 1
