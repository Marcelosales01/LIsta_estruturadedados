class OperadoresMatematicos:
    def __init__(self):
        self.pilha_operadores = []

    def identificar_operadores(self, expressao):
        for caractere in expressao:
            if caractere in {'+', '-', '*', '/', '^'}:
                self.pilha_operadores.append(caractere)

    def obter_operadores_unicos(self):
        operadores_unicos = set(self.pilha_operadores)
        return operadores_unicos

if __name__ == "__main__":
    expressao = "(2+3)*(8-9)/(7^3)"

    operadores = OperadoresMatematicos()
    operadores.identificar_operadores(expressao)

    operadores_unicos = operadores.obter_operadores_unicos()

    print(f"Expressão matemática: {expressao}")
    print("Operadores matemáticos presentes na expressão:")
    for operador in operadores_unicos:
        print(operador)
