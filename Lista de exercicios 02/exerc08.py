#Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
#“calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        total = sum(self.notas)
        media = total / len(self.notas)
        return media
    
notas_aluno1 = (8.0, 6.5, 10.0)
aluno1 = Aluno("Gabi", notas_aluno1)
media_aluno1 = aluno1.calcular_media()

print(f"A média do aluno {aluno1.nome} é:", media_aluno1)

        