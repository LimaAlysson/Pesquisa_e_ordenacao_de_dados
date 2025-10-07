import random
import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort

any_numbers = random.sample(range(1, 100), 10)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23,
28, 32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64,
63, 51, 40, 49, 42, 41, 34, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 4, 7, 1]


if __name__ == "__main__":
    # sort = heap_sort
    # test_cases = {
    #     'Números aleatórios': any_numbers,
    #     'Já ordenados': already_sorted,
    #     'Ordem inversa': inversed,
    #     'Elementos repetidos': repeated
    # }
    # print("*********************************")
    # print(f'***{sort.__name__}***')
    # for nome, lista in test_cases.items():
    #     print(f'\nCaso de teste: {nome}')
    #     print(lista)
    #     sort.heapsort(lista)
    #     print("\n Ordenado:")
    #     print(lista)

    print(any_numbers)
    print('ORDENADO')
    print(quick_sort.quick_sort(any_numbers))