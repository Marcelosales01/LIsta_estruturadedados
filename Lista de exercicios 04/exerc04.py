def encontrar_segundo_menor(vetor):
    if len(vetor) < 2:
        return None  

    menor = float('inf')
    segundo_menor = float('inf')

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    return segundo_menor

vetor = [64, 25, 7, 22, 18, 12, 7]

segundo_menor = encontrar_segundo_menor(vetor)
if segundo_menor is not None:
    print("O segundo menor número é:", segundo_menor)
else:
    print("Não foi possível encontrar o segundo menor número.")
