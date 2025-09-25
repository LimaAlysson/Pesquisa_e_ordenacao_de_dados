
def bubble_sort(lista):
    
    n = len(lista)

    for j in range(n-1):
        print(j)
        for i in range(n-1):
            print(i)
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista