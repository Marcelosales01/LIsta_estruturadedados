def fatorial(n):
    fatorial = 1
    for i in range(1,n + 1):
        fatorial *= i
    return fatorial
    
try:
    print("Calculadora de fatorial")
    num = int(input("Digite um numero inteiro e positivo: "))
    resultado = fatorial(num)
    print(f"O fatorial de {num} é igual a {resultado}")
except ValueError:
    print("Digite um numero válido")











    
