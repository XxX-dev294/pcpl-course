from .color import FigureColor
from .figure import Figure


class Rectangle(Figure):
    FIGURE_TYPE = 'Прямоугольник'

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {}, площадь {:.2f}'.format(
            self.get_figure_type(), self.color.color, self.width, self.height, self.area())
