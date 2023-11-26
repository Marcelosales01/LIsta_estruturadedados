from queue import Queue

class SistemaFilaImpressao:
    def __init__(self):
        self.fila_impressao = Queue()

    def adicionar_documento(self, documento):
        self.fila_impressao.put(documento)
        print(f"Documento '{documento}' adicionado à fila de impressão.")

    def imprimir_documentos(self):
        while not self.fila_impressao.empty():
            documento = self.fila_impressao.get()
            print(f"Imprimindo documento: '{documento}'")

if __name__ == "__main__":
    sistema_fila = SistemaFilaImpressao()

    sistema_fila.adicionar_documento("Boleto.pdf")
    sistema_fila.adicionar_documento("Apresentacao.pptx")
    sistema_fila.adicionar_documento("Relatorio.doc")
    sistema_fila.adicionar_documento("TCC.doc")

    print("\nIniciando impressão...\n")
    sistema_fila.imprimir_documentos()



        

            