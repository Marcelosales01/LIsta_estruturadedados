# Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
# algoritmo de seleção.

def ordenar_vetor(lista):
    n = len(lista)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

vetor = [99, 53, 23, 12, 33, 78]
vetor_ordenado = ordenar_vetor(vetor)
print(vetor_ordenado)


