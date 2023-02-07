from datetime import datetime


class Dog:
    def __init__(self, name: str, gender: str, age: int,
                 breed: str, preferable_meal: set, last_vet_check: datetime = None):
        """
        клас ПЕС створений для відображення життєдіяльності собак
        :param name: імя собаки
        :param gender: стать
        :param age: вік
        :param breed: порода
        :param preferable_meal: улюблена їжа
        :param last_vet_check: остання перевірка у ветеринара
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.preferable_meal = preferable_meal
        self.check_feed = True
        self.check_walk = False

        # різниця між останнім візитом
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True

    def __str__(self) -> str:
        """
        Опис собаки
        :return: інформація про собаку
        """
        return f'Собака {self.gender} породи {self.breed} на прізвисько {self.name}'

    def eat(self, food: str):
        """
        Чи подобається собаці їжа
        :param food: їжа, якою годують
        """
        if food in self.preferable_meal:
            print(f'Собака {self.name} їсть {food}')
            self.check_feed = True
        else:
            print(f'Собака {self.name} не їсть {food}')
            self.check_feed = False

    def walk(self, distance: float):
        """
        Скільки собака гуляє
        :param distance: кількість км
        """
        print(f'Собака {self.name} гуляв/ла {distance} кілометрів')
        self.check_walk = True

    def sound(self, count: int):
        """
        Скільки собака гавкає
        :param count: кількість 'гав'
        """
        for i in range(count):
            print(f'Собака {self.name} гавкає')


