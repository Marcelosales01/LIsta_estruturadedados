def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_terceiro_maior(vetor):
    selecao_ordenacao(vetor)
    if len(vetor)<=2:
        print('Vetor menor que 3 elementos')
        return None
    return vetor[2]

vetor=[5,7,3]
print(encontrar_terceiro_maior(vetor))
print(vetor)