import math
class circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * self.raio ** 2
        return area
    
raio_do_circulo = 5
circulo = circulo(raio_do_circulo)
area_do_circulo = circulo.calcular_area()
    
print(f"A área do círculo é:{area_do_circulo} cm²")