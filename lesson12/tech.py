import csv
from uuid import uuid4


def create_index(tovar_uids: dict, index_key: str) -> dict:
    """
    Функція створює індекс по збігу.
    :param tovar_uids: індекс унікальних айді для кожного запису
    :param index_key: ключ, по якому створюється індекс
    :return: new_index: створений індекс по категоріях і брендах
    """
    new_index = dict()
    for uid, tovar in tovar_uids.items():
        if tovar[index_key] in new_index:
            new_index[tovar[index_key]].append(uid)
        else:
            new_index[tovar[index_key]] = [uid]
    return new_index


def brand_in_categories(tovar_uids: dict, _categories_index: dict,
                        _categories_name: str, debug: bool = False) -> dict:
    """
    Функція, яка рахує кількість брендів в категорії.
    :param tovar_uids: індекс унікальних айді для кожного запису
    :param _categories_index: індекс категорії
    :param _categories_name: назва категорії
    :param debug: для перевірки роботи
    :return:
    """
    brand_in_cat = dict()
    for uid in _categories_index[_categories_name]:
        if debug:
            print(tovar_uids[uid])
        tovar = tovar_uids[uid]['brand']
        if tovar in brand_in_cat:
            brand_in_cat[tovar] += 1
        else:
            brand_in_cat[tovar] = 1
    return brand_in_cat


if __name__ == '__main__':
    data = {'data': list()}
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data['data'].append(row)

    # створення індексу унікальних id для кожного запису
    tovar_ids_index = dict()
    for tovar in data['data']:
        _uid = uuid4()
        tovar_ids_index[_uid] = tovar
    # print(tovar_ids_index)

    # створення індексу по категоріях та виведення кількості товарів в кожній категорії
    print('********************')
    category_index = create_index(tovar_ids_index, 'category')
    for key, value in category_index.items():
        print(f'В категорії {key} є {len(value)} найменувань')

    # створення індексу по брендах та виведення кількості товарів кожного бренду
    print('********************')
    brand_index = create_index(tovar_ids_index, 'brand')
    for key, value in brand_index.items():
        print(f'Бренд {key} є {len(value)} найменувань')

    # виведення переліку повної інформації про кожний товар одного обраного бренду
    print('********************')
    brand = 'Apple'
    print(f'Бренд "{brand}":')
    for uid in brand_index[brand]:
        print(tovar_ids_index[uid])

    # виведення переліку повної інформації про кожний товар однієї категорії
    print('********************')
    category = 'Laptop'
    print(f'Категорія "{category}":')
    for uid in category_index[category]:
        print(tovar_ids_index[uid])

    # розподіл товарів по брендах для кожної категорії
    print('********************')
    for category_name in category_index.keys():
        print(f'В категорії {category_name} представлено: ',
              brand_in_categories(tovar_ids_index, category_index, category_name))


