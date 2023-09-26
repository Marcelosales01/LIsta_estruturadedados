import re
def e_palindromo(palavra):
    palavra = re.sub(r'[^a-zA-Z]', '', palavra.lower())
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra para verificar se é palindromo: ")

if e_palindromo(palavra):
    print(f"A palavra {palavra} é palindromo")

else:
    print(f"A palavra {palavra} não é palindromo")
    