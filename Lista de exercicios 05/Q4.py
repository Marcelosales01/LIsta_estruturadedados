from queue import Queue

class ListaDeTarefas:
    def __init__(self):
        self.tarefas_pendentes = Queue()

    def adicionar_tarefa(self, tarefa):
        self.tarefas_pendentes.put(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista de tarefas.")

    def concluir_tarefas(self):
        while not self.tarefas_pendentes.empty():
            tarefa = self.tarefas_pendentes.get()
            print(f"Tarefa concluída: '{tarefa}'")

if __name__ == "__main__":
    lista_tarefas = ListaDeTarefas()

    lista_tarefas.adicionar_tarefa("Estudar Python")
    lista_tarefas.adicionar_tarefa("Fazer compras")
    lista_tarefas.adicionar_tarefa("Preparar apresentação")

    print("\nConcluindo tarefas...\n")
    lista_tarefas.concluir_tarefas()
