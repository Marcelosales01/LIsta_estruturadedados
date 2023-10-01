def encontrarElementoMax_Min(vetor):
    n = len(vetor)

    maximo = vetor[0]
    minimo = vetor[0]

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento

        elif elemento < minimo:
            minimo = elemento

    return maximo, minimo

vetor = [85,65,22,150,97,2,41,6]

maximo, minimo = encontrarElementoMax_Min(vetor)
print("Elemento maximo: ", maximo)
print("Elemento minimo: ", minimo)


