def adicao (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def divisao (a, b):
    if b == 0:
        print("Erro, Segundo valor deve ser maior que zero.")
    return a / b

def multiplicacao (a, b):
    return a * b

def calculadora():
    print("Escolha a operação a ser feita:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")

    escolha = int(input("Escolha uma opção: "))

    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))

    if escolha == 1:
        print(f"Resultado: {adicao(n1,n2)}")

    elif escolha == 2:
        print(f"Resultado: {subtracao(n1,n2)}")

    elif escolha == 3:
        print(f"Resultado: {divisao(n1,n2)}")

    elif escolha == 4:
        print(f"Resultado: {multiplicacao(n1,n2)}")

    else:
        print("Erro, informe um numero valido")

calculadora()



        
        

    

