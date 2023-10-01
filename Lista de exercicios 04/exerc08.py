def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_mediana(vetor):
    vetor_ordenado = sorted(vetor)
    n = len(vetor_ordenado)
    if n % 2 == 0:
        meio1 = vetor_ordenado[n // 2 - 1]
        meio2 = vetor_ordenado[n // 2]
        return (meio1 + meio2) / 2
    else:
        return vetor_ordenado[n // 2]

vetor=[5,7,3,9]
selecao_ordenacao(vetor)
print(encontrar_mediana(vetor))
print(vetor)