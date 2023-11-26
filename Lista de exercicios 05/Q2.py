from queue import Queue

class SistemaFilaAtendimento:
    def __init__(self):
        self.fila_atendimento = Queue()

    def entrar_na_fila(self, cliente):
        self.fila_atendimento.put(cliente)
        print(f"Cliente '{cliente}' entrou na fila de atendimento.")

    def atender_clientes(self):
        while not self.fila_atendimento.empty():
            cliente = self.fila_atendimento.get()
            print(f"Atendendo cliente: '{cliente}'")

if __name__ == "__main__":
    sistema_atendimento = SistemaFilaAtendimento()

    sistema_atendimento.entrar_na_fila("Cliente 1")
    sistema_atendimento.entrar_na_fila("Cliente 2")
    sistema_atendimento.entrar_na_fila("Cliente 3")

    print("\nIniciando atendimento...\n")
    sistema_atendimento.atender_clientes()
