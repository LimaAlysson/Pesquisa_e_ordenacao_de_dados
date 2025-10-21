#Ordenação por contagem

# Tem que inverter as duas ultimas lihas do pseudocódigo
import random 

def counting_sort(lista):
    n = len(lista)
    maior = 0
    

    for i in lista:
        if i > maior:
            maior = i

    contagem = [0] * (maior+1)

    for j in lista:
        contagem[j] += 1
    
    for k in range(1, maior+1):
        contagem[k] += contagem[k-1]
    
    saida = [0] * n

    for k in range(n-1, -1, -1):
        v = lista[k]
        saida[contagem[v] - 1] = v
        contagem[v] -= 1

    return saida

if __name__ == '__main__':
    lista = random.sample(range(1,100), 10)
    print(lista)
    teste = counting_sort(lista)
    print(teste)