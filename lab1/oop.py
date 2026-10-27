import sys
from math import sqrt


class Coefficient:

    def __init__(self, index, prompt):
        self.index = index
        self.prompt = prompt
        self.value = self._read()

    def _read(self):
        try:
            return float(sys.argv[self.index])
        except (IndexError, ValueError):
            pass
        while True:
            try:
                return float(input(self.prompt))
            except ValueError:
                print('Некорректное значение, повторите ввод.')


class BiquadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def _quadratic_roots(self):
        if self.a == 0:
            return [] if self.b == 0 else [-self.c / self.b]
        d = self.discriminant()
        if d < 0:
            return []
        sqrt_d = sqrt(d)
        return [(-self.b + sqrt_d) / (2 * self.a), (-self.b - sqrt_d) / (2 * self.a)]

    def solve(self):
        result = set()
        for t in self._quadratic_roots():
            if t > 0:
                result.update((sqrt(t), -sqrt(t)))
            elif t == 0:
                result.add(0.0)
        self.roots = sorted(result)
        return self.roots


def main():
    a = Coefficient(1, 'Введите коэффициент A: ').value
    b = Coefficient(2, 'Введите коэффициент B: ').value
    c = Coefficient(3, 'Введите коэффициент C: ').value

    equation = BiquadraticEquation(a, b, c)
    roots = equation.solve()
    if a != 0:
        print('Дискриминант: {}'.format(equation.discriminant()))
    if not roots:
        print('Действительных корней нет.')
    else:
        print('Количество действительных корней: {}'.format(len(roots)))
        for r in roots:
            print('x = {:.4f}'.format(r))


if __name__ == '__main__':
    main()
