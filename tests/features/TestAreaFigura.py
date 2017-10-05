# coding=utf-8
import unittest
from areafigura import AreaFigura

class TestAreaFigura(unittest.TestCase):

    def setUp(self):
        self.area = AreaFigura()

    def test_area_rect_5_6_igual_30(self):
        self.area.area_rectangulo(5, 6)
        self.assertEquals(self.area.get_area(), 30)

    def test_area_square_10_igual_100(self):
        self.area.area_cuadrado(10)
        self.assertEquals(self.area.get_area(), 100)

    def test_area_circle_10_igual_314(self):
        self.area.area_circulo(10)
        self.assertEquals(self.area.get_area(), 314.16)

    def test_area_trap_5_6_5_igual_27(self):
        self.area.area_trapecio(5, 6, 5)
        self.assertEquals(self.area.get_area(), 27.5)

    def tearDown(self):
        pass

if __name__ == '__main__': # pragma: no cover
    unittest.main() # pragma: no cover
