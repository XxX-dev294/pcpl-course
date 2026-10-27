import random

import cowsay
import pyjokes

from lab_python_oop import Circle
from lab_python_oop import Rectangle
from lab_python_oop import Square

N = 15
MAX_JOKE_LEN = 80


def main():
    figures = [
        Rectangle(N, N, 'синего'),
        Circle(N, 'зелёного'),
        Square(N, 'красного'),
    ]
    for figure in figures:
        print(figure)

    jokes = [j for j in pyjokes.get_jokes(category='neutral') if 50 <= len(j) <= MAX_JOKE_LEN]
    cowsay.cow(random.choice(jokes))


if __name__ == '__main__':
    main()
