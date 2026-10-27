from math import pi

from .color import FigureColor
from .figure import Figure


class Circle(Figure):
    FIGURE_TYPE = 'Круг'

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиусом {}, площадь {:.2f}'.format(
            self.get_figure_type(), self.color.color, self.radius, self.area())
