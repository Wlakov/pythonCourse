from cat import Cat
from dog import Dog
import random
from datetime import datetime, timedelta

if __name__ == '__main__':
    # create pets
    cats = list()
    dogs = list()
    cat_food = [
        'whiskas',
        'мясо',
        'рыба',
        'молоко',
        'вода',
        'сухой корм',
        'purina pro',
        'gourmet',
        'club 4 paws'
    ]
    dog_food = [
        'Royal Canin',
        'М\'ясо',
        'Вода',
        'каша'
    ]
    last_vet_check = datetime.now()
    for name in [
        'Белочка', 'Арабика', 'Пинки', 'Дымка', 'Санни', 'Тень', 'Бланка', 'Лили', 'Фокси', 'Блэки', 'Полоска',
        'Брауни', 'Злата'
    ]:
        last_vet_check -= timedelta(days=30)
        cats.append(Cat(
            name=name,
            gender=random.choice(['кот', 'кошка']),
            age=random.randint(1, 15),
            breed='',
            preferable_meal=set(random.choices(cat_food, k=5)),
            last_vet_check=last_vet_check
        ))

    # performing pet everyday lifestyle
    for cat in cats:
        cat.sleep(4)
        for food in random.choices(cat_food, k=5):
            cat.eat(food)

    # check if all pets are good
    for cat in cats:
        print(f'Проверяем всё ли хорошо с {cat}')
        if not cat.fed_check:
            if cat.gender == 'кошка':
                print(f'Warning! {cat.name} голодна!')
            elif cat.gender == 'кот':
                print(f'Warning! {cat.name} голоден!')
            else:
                print(f'{cat.name} - unknown gender {cat.gender}!')
        if not cat.vet_check:
            if cat.gender == 'кошка':
                print(f'Warning! {cat.name} давно не проверялась у ветеринара!')
            elif cat.gender == 'кот':
                print(f'Warning! {cat.name} давно не проверялся у ветеринара!')
            else:
                print(f'{cat.name} - unknown gender {cat.gender}!')

    print('---------------')

    last_vet_check = datetime.now()
    for name in [
        'Тіма', 'Джек', 'Малюк', 'Майор Булочка', 'Рекс', 'Рижик', 'Морті'
    ]:
        last_vet_check -= timedelta(days=60)  # у кожен запис останній візит був -60 днів від попереднього собаки
        dogs.append(Dog(
            name=name,
            gender=random.choice(['хлопак', 'дівчина']),
            age=random.randint(1, 12),
            breed=random.choice(['такса', 'вівчарка', 'американський бульдог', 'лабрадор']),
            preferable_meal=set(random.choices(dog_food, k=3)),
            last_vet_check=last_vet_check
        ))

    # їмо
    for dog in dogs:
        for food in random.choices(dog_food, k=1):
            dog.eat(food)

    # гавкаємо
    for dog in dogs:
        dog.sound(random.randint(1, 3))

    # гуляємо
    for dog in random.choices(dogs, k=5):
        dog.walk(round(random.uniform(1, 4), 2))

    # перевірка
    i = 1  # номер запису
    for dog in dogs:
        print(f'{i}.{dog}')
        if not dog.check_walk:
            print(f'  Собака {dog.name} сьогодні не гуляв/-ла!')
        if not dog.check_feed:
            print(f'  Собака {dog.name} голодний/-а!')
        if not dog.vet_check:
            print(f'  Собаці {dog.name} треба до ветеринара ')
        i += 1
