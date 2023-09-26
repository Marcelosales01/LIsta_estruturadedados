def e_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Digite um numero inteiro para verificar se é primo: "))

if e_primo(num):
    print("É primo.")
else:
    print("Não é primo.")
