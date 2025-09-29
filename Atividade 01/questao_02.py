import random 

def bubble_sort_alter(lista):

    n = len(lista)

    for j in range(n):
        #print(j)
        swapped = False
        for i in range(n - j - 1):
            #print(lista[i], lista[i+1])
            if lista[i] > lista[i+1]:
                swapped = True
                lista[i], lista[i+1] = lista[i+1], lista[i]

        if not swapped:
            return lista

    return lista

if __name__ == '__main__':
    lista = random.sample(range(1, 100), 10)
    print("\n*** LISTA DESORDENADA ***")
    print(lista)
    print("\n*** BUBBLE SORT ALTERADO ***")
    print(bubble_sort_alter(lista))


# ***ANÁLISE DE CUSTO DA FUNÇÃO***
# MELHOR CASO: O algoritmo executa apenas o primeiro laço externo (j=0) No laço interno, percorre todos os n-1 elementos uma vez Como não há trocas, swapped permanece False A condição if not swapped é verdadeira, então o algoritmo retorna imediatamente Total: n-1 comparações = O(n)
# PIOR CASO: Quando ocorre: Quando a lista está ordenada em ordem decrescente (completamente invertida). Por que: O algoritmo executa todos os n passes do laço externo Em cada passe j, executa (n-j-1) comparações no laço interno Total de comparações: (n-1) + (n-2) + (n-3) + ... + 1 = n(n-1)/2 = O(n²)


# Equipe: Alysson José, André Igor, Leonardo Lucena