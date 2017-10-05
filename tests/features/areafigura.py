import math

class AreaFigura():

    def __init__(self):
        self.area = 0

    def area_rectangulo(self, base, height):
        self.area = base * height

    def area_cuadrado(self, side):
        self.area = side ** 2

    def area_trapecio(self, mayor_base, minor_base, height):
        self.area = (mayor_base + minor_base) * height / 2.0

    def area_circulo(self,radius):
        self.area = round(3.1416 * radius ** 2, 2)

    def get_area(self):
        return self.area
