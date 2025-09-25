
def selection_sort(lista):
    n = len(lista)
    
    for j in range(n-1):
        min_indice = j

        for i in range(j, n):
            if lista[i] < lista[min_indice]:
                min_indice = i

        if lista[j] > lista[min_indice]:
            lista[j], lista[min_indice] = lista[min_indice], lista[j]
            #aux = lista[j]
            #lista[j] = lista[min_indice]
            #lista[min_indice] = aux 
    return lista