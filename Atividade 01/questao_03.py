import random
from questao_01 import bubble_sort

def k_esimo_menor(lista, k):
    
    lista_ordenada = bubble_sort(lista)
    n = len(lista)

    if k > n or k < 1:
        print('Erro')
        return None
    
    return lista_ordenada[k-1]

if __name__ == '__main__':
    lista = random.sample(range(1, 100), 10)
    print(f'\nLista desordenada: {lista}')
    print(f'k-ésimo menor elemento: {k_esimo_menor(lista, 2)}')


# ***ANÁLISE DE CUSTO DA FUNÇÃO***
# A complexidade da função acima é determinada pela função Bubble Sort - O(n²). Todas as outras operações tem tempo constante O(1). Sendo assim, o termo de maior ordem determina o resultando final. O custo da função é O(n²).


# Equipe: Alysson José, André Igor, Leonardo Lucena