#Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
#método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = (preço)
        self.quantidade = (quantidade)

    def calcular_total(self):
        self.preço * self.quantidade

produto1 = Produto("Copo", 10, 5)    
total1 = produto1.calcular_total()
print(f"Total do {produto1.nome}: R$ {total1}")




