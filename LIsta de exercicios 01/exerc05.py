numeros = [1, 12, 43, 75, 24, 21]
numeros = [int(num) for num in numeros if int(num) % 2 ==0]

if numeros:
    media_numeros = sum(numeros) / len(numeros)

    print(numeros)
    print(" A média dos números pares é: ", media_numeros)


    