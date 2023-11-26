from queue import Queue

class SistemaGerenciamentoPedidos:
    def __init__(self):
        self.fila_pedidos = Queue()

    def fazer_pedido(self, pedido):
        self.fila_pedidos.put(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")

    def processar_pedidos(self):
        while not self.fila_pedidos.empty():
            pedido = self.fila_pedidos.get()
            print(f"Processando pedido: '{pedido}'")

if __name__ == "__main__":
    sistema_pedidos = SistemaGerenciamentoPedidos()

    sistema_pedidos.fazer_pedido("Pizza Margherita")
    sistema_pedidos.fazer_pedido("Hambúrguer com batatas fritas")
    sistema_pedidos.fazer_pedido("Sushi")

    print("\nIniciando processamento de pedidos...\n")
    sistema_pedidos.processar_pedidos()
