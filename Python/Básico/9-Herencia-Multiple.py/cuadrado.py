from HerenciaMultiple import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):# Agregamos las clases padre de las que hereda
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)


    def calcular_area(self):
        return self.alto * self.ancho