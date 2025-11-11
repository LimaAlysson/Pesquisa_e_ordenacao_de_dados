
from random import sample
# Complexidade = O(logn)

def busca_binaria(lista, x, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == x:
            return meio
        if x < lista[meio]:
            return busca_binaria(lista, x, inicio, meio-1)
        else:
            return busca_binaria(lista, x, meio+1, fim)
    return -1


lista = [1,1,2,3,4,5,6,7,8,9,10]

busca = busca_binaria(lista, 1)
print(busca)