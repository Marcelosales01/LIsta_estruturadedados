def calcular_imc(peso, altura):
    imc = (peso/(altura * altura))
    return imc



peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)
print("O IMC é de: ", imc)



