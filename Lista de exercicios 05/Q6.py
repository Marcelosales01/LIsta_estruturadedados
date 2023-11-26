class NavegadorWeb:
    def __init__(self):
        self.historico = []
        self.pagina_atual = None

    def visitar_pagina(self, pagina):
        if self.pagina_atual is not None:
            self.historico.append(self.pagina_atual)
        self.pagina_atual = pagina
        print(f"Visitando página: {pagina}")

    def voltar(self):
        if self.historico:
            self.pagina_atual = self.historico.pop()
            print(f"Voltando para página: {self.pagina_atual}")
        else:
            print("Não há histórico para voltar.")

    def avancar(self):
        if self.pagina_atual is not None:
            print("Não é possível avançar, pois não há histórico futuro.")
        elif self.historico:
            self.pagina_atual = self.historico.pop()
            print(f"Indo para a frente para página: {self.pagina_atual}")
        else:
            print("Não há histórico para avançar.")

if __name__ == "__main__":
    navegador = NavegadorWeb()

    navegador.visitar_pagina("www.google.com")
    navegador.visitar_pagina("www.wikipedia.org")
    navegador.visitar_pagina("www.github.com")

    navegador.voltar()
    navegador.avancar()
    navegador.voltar()
    navegador.voltar()
    navegador.avancar()
