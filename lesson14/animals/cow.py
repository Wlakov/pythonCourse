from .animal import Animal
from datetime import datetime


class Cow(Animal):
    def __init__(self, name: str, age: int, last_vet_check: datetime = None):
        super().__init__(f'корова {name}', {'трава', 'сіно'}, age)
        self.say_word = 'Мууу'
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference >= 6:
                self.vet_check = False
            else:
                self.vet_check = True

    # перевизначення методу
    """def say(self):
        print(f'{self.name} привертає ваше увагу "Мууу"')"""
    """def say(self, count: int):
        for i in range(count):
            print(f'{self.name} привертає ваше увагу "Мууу"')"""

    def moo(self, count: int):
        for i in range(count):
            print(f'{self.name} каже "Муууу"')

    def treat(self) -> str:
        print(f'Ви доглядаєте за {self.name} і корова дає молоко')
        return 'Відро молока'


if __name__ == '__main__':
    c = Cow('Бурьонка', 3)
    print(c)
    c.eat('м\'ясо')
    c.eat('трава')
    c.say(3)
    c.moo(3)
    print(c.treat())
    print(isinstance(c, Cow))
    print(isinstance(c, Animal))
