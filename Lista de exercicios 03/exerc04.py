def soma_digitos(num):
    soma = 0

    num_str = str(num)

    for digito in num_str:
        soma += int(digito)
    return soma

num = int(input("Digite um numero inteiro e positivo: "))

if num < 0:
    print("Digite um número válido.")
else:
    resultado = soma_digitos(num)

    print(f"O valor dos digitos {num} somados é igual a {resultado}")

