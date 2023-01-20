def get_sides_from_user() -> int:
    """
    Функція отримання вводу користувача
    :return: отримані від користувача дані
    """
    num1 = input('Input 1: ')
    num1 = int(num1)
    num2 = input('Input 2: ')
    num2 = int(num2)
    num3 = input('Input 3: ')
    num3 = int(num3)
    return num1, num2, num3


def check_ex(num1, num2, num3):
    """
    Перевірка на правильність трикутника
    :param num1: 1 сторона
    :param num2: 2 сторона
    :param num3: 3 сторона
    :return:вірні сторони
    """
    if (num1 + num2) < num3 or (num2 + num3) < num1 or (num1 + num3) < num2:
        print('triangle doesnt exist')
        return False
    else:
        return num1, num2, num3


def calc_p(side1, side2, side3) -> int:
    """
    Функція підрахунку периметру
    :param num1: 1 сторона
    :param num2: 2 сторона
    :param num3: 3 сторона
    :return: периметр
    """
    p = (side1 + side2 + side3) / 2
    print(f'Периметр трикутника зі стронами {side1}, {side2}, {side3} дорівнює {p}')
    return p


def calc_s(side1, side2, side3, p):
    """
    Функція підрахунку площі
    :param num1: 1 сторона
    :param num2: 2 сторона
    :param num3: 3 сторона
    :param p: периметр
    """
    s = pow(p * (p - side1) * (p - side2) * (p - side3), 1 / 2)
    print(f'Площа трикутника зі стронами {side1}, {side2}, {side3} дорівнює {s}')


if __name__ == '__main__':
    while True:
        side1, side2, side3 = get_sides_from_user()
        while True:
            if check_ex(side1, side2, side3):
                p = calc_p(side1, side2, side3)
                calc_s(side1, side2, side3, p)
                break
            else:
                break