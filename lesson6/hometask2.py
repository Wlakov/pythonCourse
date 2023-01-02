def get_sides_from_user() -> int:  # функція отримання вводу користувача
    while True:
        try:
            num1 = input('Input 1: ')
            num1 = int(num1)
            num2 = input('Input 2: ')
            num2 = int(num2)
            num3 = input('Input 3: ')
            num3 = int(num3)
            if (num1 + num2) < num3 or (num2 + num3) < num1 or (num1 + num3) < num2:  # перевірка на правильність
                # трикутника
                print('error')
                continue
            return num1, num2, num3
        except Exception:
            print('Error,try again')


def calc_triangle() -> int:  # функція підрахунку периметру та площі
    side1, side2, side3 = get_sides_from_user()
    p = (side1 + side2 + side3) / 2
    s = pow(p * (p - side1) * (p - side2) * (p - side3), 1 / 2)
    print(f'Периметр трикутника зі стронами {side1}, {side2}, {side3} дорівнює {p}')
    print(f'Площа трикутника зі стронами {side1}, {side2}, {side3} дорівнює {s}')


if __name__ == '__main__':
    while True:
        calc_triangle()
