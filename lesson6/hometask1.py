# Показати звичайний текст
def display_menu():
    print('Обрахунок комунальних послуг\n'
          'Під час обрахунку використовуються перші 5 цифр на газовому лічильнику\n'
          'Але БЕЗ нулів на початку')


def calculate_pokazniki():  # функція для присвоєння змінним значень фукццій
    display_menu()
    num1, num2 = get_pokazniki_from_user()
    input_tariff = choose_tariff()
    tariff(input_tariff, num1, num2)


def choose_tariff(lower_bound: int = 1, upper_bound: int = 3) -> int:  # функція вибору тарифу
    while True:
        try:
            print("""Виберіть тариф(числом) 
            1-Волинська область( 7.98 грн/м.куб) 
            2-Дніпропетровська область( 8.46 грн/м.куб)
            3-Київська область (9.95 грн/м.куб)""")
            input_tariff = input('Виберіть : ')
            input_tariff = int(input_tariff)
            if input_tariff < lower_bound or input_tariff > upper_bound:
                raise ValueError
            return input_tariff
        except Exception:
            print('Error,try again')


def tariff(input_tariff, num1, num2) -> int:  # функція обрахунку показників за тарифом
    if input_tariff == 1:
        x = (num2 - num1) * 7.98
        print(f'Сума до сплати:{round(x, 2)} гривень')
    elif input_tariff == 2:
        x = (num2 - num1) * 8.46
        print(f'Сума до сплати:{round(x, 2)} гривень')
    elif input_tariff == 3:
        x = (num2 - num1) * 9.95
        print(f'Сума до сплати:{round(x, 2)} гривень')
    else:
        exit()


def get_pokazniki_from_user() -> int:  # функція отримання показників лічильника від користувача
    num1 = ''
    num2 = ''
    while True:
        try:
            num1 = input('Input past pokaznik: ')
            num1 = int(num1)
            num2 = input('Input present pokaznik: ')
            num2 = int(num2)
            if num1 > num2:
                print('error')
                continue
            return num1, num2
        except Exception:
            print('Error,try again')


if __name__ == '__main__':
    while True:
        calculate_pokazniki()
