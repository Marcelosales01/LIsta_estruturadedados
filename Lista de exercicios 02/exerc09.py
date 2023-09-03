#Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
#método chamado “calcular_perimetro” que retorna o perímetro do triângulo

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
triangulo1 = Triangulo(2,4,6)
perimetro = triangulo1.calcular_perimetro()
print("O perimetro do triangulo é:", perimetro)