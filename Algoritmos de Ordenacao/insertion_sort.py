#utilizando while
def insertion_sort_while(lista):

    n = len(lista)

    for i in range(1, n):
        chave = lista[i]
        j = i-1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    
    return lista

#utilizando for
def insertion_sort_for(lista):

    n = len(lista)

    for i in range(1, n):
        chave = lista[i]
        posicao_insercao = i

        for j in range (i-1, -1, -1):
            if lista[j] > chave:
                lista[j+1] = lista[j]
                posicao_insercao = j
            else:
                break
        lista[posicao_insercao] = chave
    
    return lista