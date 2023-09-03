#Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
#método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
#do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, porcentagem_aumento):
        if porcentagem_aumento > 0:
            aumento = (porcentagem_aumento / 100) * self.salario
            self.salario += aumento
            return f"Salario do funcionario {self.nome} atualizado para {self.salario}"
        else:
            return "Percentual de aumento deve ser maior que zero."
        
funcionario1 = Funcionario("Bruno", 2000.00, "gerente")
print(funcionario1.aumentar_salario(50))
