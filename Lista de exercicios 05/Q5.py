from queue import Queue

class FilaPedidosOnline:
    def __init__(self):
        self.fila_pedidos = Queue()

    def adicionar_pedido(self, pedido):
        self.fila_pedidos.put(pedido)
        print(f"Pedido online '{pedido}' adicionado à fila.")

    def processar_pedidos(self):
        while not self.fila_pedidos.empty():
            pedido = self.fila_pedidos.get()
            print(f"Processando pedido online: '{pedido}'")

if __name__ == "__main__":
    fila_pedidos_online = FilaPedidosOnline()

    fila_pedidos_online.adicionar_pedido("Produto A")
    fila_pedidos_online.adicionar_pedido("Produto B")
    fila_pedidos_online.adicionar_pedido("Produto C")

    print("\nIniciando processamento de pedidos online...\n")
    fila_pedidos_online.processar_pedidos()
