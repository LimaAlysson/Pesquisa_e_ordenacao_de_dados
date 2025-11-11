
def busca_binaria(lista, x, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == x:
            posicoes = [meio]
            
            i = meio - 1
            while i >= 0 and lista[i] == x:
                print(lista[i], x)
                posicoes.append(i)
                i -= 1

            j = meio + 1
            while j < fim+1 and lista[j] == x:
                posicoes.append(j)
                j += 1

            return posicoes
            
        if x < lista[meio]:
            return busca_binaria(lista, x, inicio, meio-1)
        else:
            return busca_binaria(lista, x, meio+1, fim)
        
    return -1

lista = [1,1,2,3,4,5,5,7,8,9,9]

busca = busca_binaria(lista, 5)
print(f'Posições encontradas para o item buscado:', busca)