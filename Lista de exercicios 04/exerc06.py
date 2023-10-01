def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def contar_par_imp(vetor):
    n = len(vetor)
    cp=0
    ci=0
    for i in range(n):
        if (vetor[i]%2==0):
            cp+=1
        else:
            ci+=1
    return cp,ci

vetor=[5,7,2,3]
selecao_ordenacao(vetor)
ct=contar_par_imp(vetor)
print(ct[0],ct[1])