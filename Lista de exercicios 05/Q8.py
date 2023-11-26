class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.historico_undo = []
        self.historico_redo = []

    def inserir_texto(self, texto):
        self.historico_undo.append(self.texto)
        self.texto += texto
        self.historico_redo = []  # Limpar o histórico de "Refazer"
        print(f"Texto inserido: '{texto}'")

    def remover_texto(self, quantidade):
        if quantidade > len(self.texto):
            raise ValueError("Não há texto suficiente para remover.")

        self.historico_undo.append(self.texto)
        texto_removido = self.texto[-quantidade:]
        self.texto = self.texto[:-quantidade]
        self.historico_redo = []  # Limpar o histórico de "Refazer"
        print(f"Texto removido: '{texto_removido}'")

    def desfazer(self):
        if not self.historico_undo:
            print("Não há ações para desfazer.")
            return

        acao_desfeita = self.historico_undo.pop()
        self.historico_redo.append(self.texto)
        self.texto = acao_desfeita
        print("Desfeito.")

    def refazer(self):
        if not self.historico_redo:
            print("Não há ações para refazer.")
            return

        acao_refeita = self.historico_redo.pop()
        self.historico_undo.append(self.texto)
        self.texto = acao_refeita
        print("Refeito.")

    def exibir_texto(self):
        print("Texto atual:", self.texto)

if __name__ == "__main__":
    editor = EditorDeTexto()

    editor.inserir_texto("Olá, ")
    editor.inserir_texto("mundo!")
    editor.exibir_texto()

    editor.desfazer()
    editor.exibir_texto()

    editor.refazer()
    editor.exibir_texto()
