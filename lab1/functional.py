import sys
from math import sqrt


def read_coef(index, prompt):
    def ask():
        try:
            return float(input(prompt))
        except ValueError:
            print('Некорректное значение, повторите ввод.')
            return ask()

    try:
        return float(sys.argv[index])
    except (IndexError, ValueError):
        return ask()


def t_roots(a, b, c):
    match (a, b):
        case (0, 0):
            return ()
        case (0, _):
            return (-c / b,)
        case _:
            d = b * b - 4 * a * c
            match d:
                case _ if d < 0:
                    return ()
                case 0:
                    return (-b / (2 * a),)
                case _:
                    return ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))


def x_roots(t):
    match t:
        case 0:
            return (0.0,)
        case _ if t > 0:
            return (sqrt(t), -sqrt(t))
        case _:
            return ()


def solve(a, b, c):
    return sorted({x for t in t_roots(a, b, c) for x in x_roots(t)})


def main():
    a = read_coef(1, 'Введите коэффициент A: ')
    b = read_coef(2, 'Введите коэффициент B: ')
    c = read_coef(3, 'Введите коэффициент C: ')

    roots = solve(a, b, c)
    if a != 0:
        print('Дискриминант: {}'.format(b * b - 4 * a * c))
    match roots:
        case []:
            print('Действительных корней нет.')
        case _:
            print('Количество действительных корней: {}'.format(len(roots)))
            for r in roots:
                print('x = {:.4f}'.format(r))


if __name__ == '__main__':
    main()
