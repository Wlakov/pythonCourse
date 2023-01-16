def show_commands(command: list):
    """
    Функція, яка виводить в консолі список команд
    :param command: ім'я списку
    """
    for com in command:
        print(com)


def get_command():
    """
    Функія, яка отримує введення користувача
    :return: повертає введений текст
    """
    user_command = input(">")
    return user_command


def readlines_file(filename: str):
    """
    Функція читає текстовий файл, користуючись вбудованою функцією readlines
    :param filename: ім'я файлу для читання
    """
    try:
        with open(filename, mode='r') as f:
            notes_list = []
            for line in f.readlines():
                reformated_line = line.replace('\n', '')
                notes_list.append(reformated_line)
            return notes_list
    except:
        print('Щось сталося під час відкриття файлу')
        exit()


def add(filename: str):
    """
    Функція, яка додає нотатку
    :param filename: ім'я файлу для читання
    """
    note = input("Введіть нотатку: ")
    with open(filename, mode='a') as f:
        f.write(f'\n{note}')


def earliest(my_notes:list):
    """
    Функція, яка виводить від найранішої до найпізнішої нотатки
    :param my_notes: ім'я списку
    """
    print("Від найранішої до найпізнішої")
    for note in my_notes:
        print(f'>{note}')


def latest(my_notes:list):
    """
    Функція, яка виводить від найпізнішої до найранішої
    :param my_notes: ім'я списку
    """
    print("Від найпізнішої до найранішої")
    for note in my_notes[::-1]:
        print(f'>{note}')


def shortest(notes: list):
    """
    Вивід від найменшої за довжиною нотатки
    :param notes: ім'я списку
    """
    sorted_n = sorted(notes, key=len)
    for note in sorted_n:
        print(f'>{note}')


def longest(notes: list):
    """
    Вивід від найбільшої за довжиною нотатки
    :param notes: ім'я списку
    """
    sorted_n = sorted(notes, reverse=True, key=len)
    for note in sorted_n:
        print(f'>{note}')


def start(notes: list, file_txt: str):
    """
    Функція, яка отримує список і маніпулює ним в залежності від команди
    :param notes: ім'я списку
    :param file_txt: ім'я файлу в який записуються нотатки
    """
    command = get_command()
    if command == 'add':
        add(file_txt)
        print(notes)
    elif command == 'earliest':
        earliest(notes)
    elif command == 'latest':
        latest(notes)
    elif command == 'longest':
        longest(notes)
    elif command == 'shortest':
        shortest(notes)
    elif command == 'exit':
        exit()
    else:
        print('Try again')


if __name__ == '__main__':
    commands = [  # список команди у записнику
        'add',
        'earliest',
        'latest',
        'longest',
        'shortest',
        'save & exit'
    ]
    notes_txt = 'notes.txt'
    show_commands(commands)
    while True:
        notes = readlines_file('notes.txt')  # файл конвертований у список
        start(notes, notes_txt)
