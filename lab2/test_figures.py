import unittest
from math import pi

from lab_python_oop import Circle
from lab_python_oop import Figure
from lab_python_oop import Rectangle
from lab_python_oop import Square


class TestFigures(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(Rectangle(3, 4, 'синего').area(), 12)

    def test_circle_area(self):
        self.assertAlmostEqual(Circle(2, 'зелёного').area(), pi * 4)

    def test_square_area(self):
        self.assertEqual(Square(5, 'красного').area(), 25)

    def test_square_is_rectangle(self):
        self.assertIsInstance(Square(1, 'красного'), Rectangle)

    def test_figure_is_abstract(self):
        with self.assertRaises(TypeError):
            Figure()

    def test_figure_type(self):
        self.assertEqual(Square.get_figure_type(), 'Квадрат')
        self.assertEqual(Circle.get_figure_type(), 'Круг')

    def test_color_property(self):
        r = Rectangle(1, 1, 'синего')
        r.color.color = 'белого'
        self.assertEqual(r.color.color, 'белого')

    def test_repr(self):
        self.assertEqual(repr(Square(2, 'красного')),
                         'Квадрат красного цвета со стороной 2, площадь 4.00')


if __name__ == '__main__':
    unittest.main()
