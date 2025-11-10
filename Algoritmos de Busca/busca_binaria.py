from random import sample

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


lista = sample(range(1, 11), 10)
lista = sorted(lista)

busca = busca_binaria(lista, 1)
print(busca)