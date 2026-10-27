import sys
from math import sqrt


def get_coef(index, prompt):
    try:
        coef = float(sys.argv[index])
    except (IndexError, ValueError):
        coef = None
    while coef is None:
        try:
            coef = float(input(prompt))
        except ValueError:
            print('Некорректное значение, повторите ввод.')
    return coef


def get_roots(a, b, c):
    if a == 0:
        if b == 0:
            return []
        t_list = [-c / b]
    else:
        d = b * b - 4 * a * c
        if d < 0:
            return []
        sqrt_d = sqrt(d)
        t_list = [(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)]

    result = set()
    for t in t_list:
        if t > 0:
            result.add(sqrt(t))
            result.add(-sqrt(t))
        elif t == 0:
            result.add(0.0)
    return sorted(result)


def main():
    a = get_coef(1, 'Введите коэффициент A: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    roots = get_roots(a, b, c)
    if a != 0:
        print('Дискриминант: {}'.format(b * b - 4 * a * c))
    if not roots:
        print('Действительных корней нет.')
    else:
        print('Количество действительных корней: {}'.format(len(roots)))
        for r in roots:
            print('x = {:.4f}'.format(r))


if __name__ == '__main__':
    main()
