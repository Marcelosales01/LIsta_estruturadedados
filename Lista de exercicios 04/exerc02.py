def ordenar_vetor(vetor, crescente=True):
    n = len(vetor)

    for i in range (n):
        extremo_index = i

        for j in range(i+1,n):
            if crescente:
                if vetor[j] < vetor[extremo_index]:
                    extremo_index = j

            else: 
                if vetor[j] > vetor[extremo_index]:
                    extremo_index = j

        vetor[i], vetor[extremo_index] = vetor[extremo_index], vetor[i]

    return vetor
    
vetor = [5,78,33,21,2,89,7]

vetor_crescente = ordenar_vetor(vetor, crescente=True)
print("Ordenação crescente: ", vetor_crescente)

vetor_decrescente = ordenar_vetor(vetor, crescente=False)
print("Ordenação decrescente: ", vetor_decrescente)
