def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Menu")
    print("1. Converter de celsius para fahrenheit")
    print("2. Converter fahrenheit para celsius")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        celsius = float(input("Digite a temperatura em celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus celsius é igual a {fahrenheit} graus fahrenheit.")

    elif escolha ==2:
        fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus fahrenheit é igual a {celsius} graus celsius.")

    else:
        print("Opção invalida, informe 1 ou 2.")

if __name__ == "__main__":
    main()
