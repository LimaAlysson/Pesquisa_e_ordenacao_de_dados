
def InsertionSort(lista_ordenada, novo_elemento):
    lista_ordenada.append(novo_elemento)
    
    i = len(lista_ordenada) - 1
    aux = lista_ordenada[i]
    
    while i > 0 and aux < lista_ordenada[i-1]:
        lista_ordenada[i] = lista_ordenada[i-1]
        i -= 1
    
    lista_ordenada[i] = aux
    
    return lista_ordenada

lista_ordenada = [2, 5, 8, 10, 13]
novo_numero = 7

print(InsertionSort(lista_ordenada, novo_numero))


# ***ANÁLISE DE CUSTO DA FUNÇÃO***
# Melhor Caso: O(1)
# Quando o novo elemento é maior que todos os elementos existentes nenhum deslocamento será necessário, apenas um append no final, sem precisar que o loop seja executado.

# Caso Médio: O(n)
# Ocorre quando o novo elemento é inserido em algum ponto do meio.Exemplo: Inserir 7 em [2, 5, 8, 10, 13]. Mesmo deslocando apenas n/2 elementos em média, na análise assintótica (Big O) vamos considerar: n/2 = O(n). O crescimento ainda é linear em relação ao tamanho da lista.

# Pior Caso: O(n)
# Ocorre quando o novo elemento é menor que todos os elementos existentes, nesse caso todos os n elementos terão de ser deslocados uma posição.


# Equipe: Alysson José, André Igor, Leonardo Lucena