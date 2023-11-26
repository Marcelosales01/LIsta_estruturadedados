class VerificadorPalindromo:
    def __init__(self):
        self.pilha = []

    def limpar_texto(self, texto):
        return ''.join(caractere.lower() for caractere in texto if caractere.isalnum())

    def e_palindromo(self, texto):
        texto_limpo = self.limpar_texto(texto)
        for caractere in texto_limpo:
            self.pilha.append(caractere)

        inverso = ''.join(self.pilha[::-1])

        return texto_limpo == inverso

if __name__ == "__main__":
    verificador = VerificadorPalindromo()

    palavra_1 = "radar"
    palavra_2 = "Python"
    frase_1 = "Ame a ema"
    frase_2 = "O rato roeu a roupa do rei de Roma"

    print(f"{palavra_1} é palíndromo? {verificador.e_palindromo(palavra_1)}")
    print(f"{palavra_2} é palíndromo? {verificador.e_palindromo(palavra_2)}")
    print(f"{frase_1} é palíndromo? {verificador.e_palindromo(frase_1)}")
    print(f"{frase_2} é palíndromo? {verificador.e_palindromo(frase_2)}")
