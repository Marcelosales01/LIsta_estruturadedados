#Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
#métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Deposito de {valor} realizado com sucesso, saldo atual: {self.saldo}"
        else:
            return "Valor de deposito invalido, necessario ser maior que zero"
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}"
        else:
            return "Saque invalido, o saque so pode ser feito com o saldo disponivel na conta."
        
    def consultar_saldo(self):
        return f"Saldo disponivel do titular {self.titular} : {self.saldo}"
    
minha_conta = ContaBancaria ("Marcelo")

print(minha_conta.consultar_saldo())
print(minha_conta.depositar(500))
print(minha_conta.sacar(200))
