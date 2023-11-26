class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def calcular(self, expressao):
        tokens = expressao.split()

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.pilha.append(float(token))
            elif token in {'+', '-', '*', '/'}:
                if len(self.pilha) < 2:
                    raise ValueError("Expressão inválida: não há operandos suficientes para o operador.")
                operando2 = self.pilha.pop()
                operando1 = self.pilha.pop()

                if token == '+':
                    resultado = operando1 + operando2
                elif token == '-':
                    resultado = operando1 - operando2
                elif token == '*':
                    resultado = operando1 * operando2
                elif token == '/':
                    if operando2 == 0:
                        raise ValueError("Divisão por zero não é permitida.")
                    resultado = operando1 / operando2

                self.pilha.append(resultado)
            else:
                raise ValueError(f"Token inválido: {token}")

        if len(self.pilha) != 1:
            raise ValueError("Expressão inválida: a pilha não contém um resultado final.")
        
        return self.pilha[0]

if __name__ == "__main__":
    calculadora = CalculadoraRPN()

    expressao_rpn = "3 4 + 2 *"
    resultado = calculadora.calcular(expressao_rpn)
    print(f"Resultado da expressão '{expressao_rpn}': {resultado}")
