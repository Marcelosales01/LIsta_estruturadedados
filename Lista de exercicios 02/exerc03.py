#Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
#chamado “calcular_area” que retorna a área do retângulo.

class retangulo:
    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area
    
base_retangulo = 5
altura_retangulo = 4
retangulo = retangulo(base_retangulo, altura_retangulo)
area_retangulo = retangulo.calcular_area()

print(f"A área do retangulo com base: {base_retangulo} e altura: {altura_retangulo} é igual a :", area_retangulo)

