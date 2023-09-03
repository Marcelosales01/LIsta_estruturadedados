# Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do livro.

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título = {self.titulo}, Autor = {self.autor}"

livro1 = livro('1984', 'George Orwell')
livro_infos = livro1.detalhes()
print(f"Os detalhes do livro são: {livro_infos}.")

    