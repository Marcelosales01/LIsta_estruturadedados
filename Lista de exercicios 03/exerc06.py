def contar(palavra):
    vogal = "aeiouAEIOU"
    num_vogal = 0

    for char in palavra:
        if char in vogal:
            num_vogal +=1

    return num_vogal

palavra_usuario = str(input("Digite uma palavra ou frase: "))
num_vogal = contar(palavra_usuario)

print("A quantidade de vogais nessa palavra ou frase é: ", num_vogal)
