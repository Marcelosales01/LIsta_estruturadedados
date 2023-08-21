# jogo pedra papel e tesoura

print("Bem vindo ao pedra, papel e tesoura!!")
escolha_user = input("Digite sua escolha: ")

if escolha_user == 'pedra':
    import random
    escolhas = ['pedra', 'papel', 'tesoura']
    palavra_aleatoria = random.choice(escolhas)

    if palavra_aleatoria == 'papel':
        print(palavra_aleatoria,)
        print("Perdeu!")

    if palavra_aleatoria == 'tesoura':
        print(palavra_aleatoria)
        print("Ganhou :)")

    if palavra_aleatoria == 'pedra':
        print("Empatou")

if escolha_user == 'papel':
    import random
    escolhas = ['pedra', 'papel', 'tesoura']
    palavra_aleatoria = random.choice(escolhas)

    if palavra_aleatoria == 'tesoura':
        print(palavra_aleatoria,)
        print("Perdeu!")

    if palavra_aleatoria == 'pedra':
        print(palavra_aleatoria)
        print("Ganhou :)")

    if palavra_aleatoria == 'papel':
        print(palavra_aleatoria)
        print("Empatou")

if escolha_user == 'tesoura':
    import random
    escolhas = ['pedra', 'papel', 'tesoura']
    palavra_aleatoria = random.choice(escolhas)


    if palavra_aleatoria == 'pedra':
        print(palavra_aleatoria,)
        print("Perdeu!")

    if palavra_aleatoria == 'papel':
        print(palavra_aleatoria)
        print("Ganhou :)")

    if palavra_aleatoria == 'tesoura':
        print(palavra_aleatoria)
        print("Empatou")

else:
    print('Erro')




