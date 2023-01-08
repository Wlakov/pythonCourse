def show_commands(command: list):  # функція, яка виводить в консолі список команд
    for com in command:
        print(com)


def get_command():  # функія, яка отримує введення користувача
    user_command = input(">")
    return user_command  # і повертає його


def add(notes):  # функція, яка додає нотатку
    note = input("Введіть нотатку: ")
    notes.append(note)


def earliest(my_notes):  # функція, яка виводить від найранішої до найпізнішої нотатки
    print("Від найранішої до найпізнішої")
    for note in my_notes:
        print(f'>{note}')


def latest(my_notes):  # функція, яка виводить від найпізнішої до найранішої
    print("Від найпізнішої до найранішої")
    for note in my_notes[::-1]:
        print(note)


def shortest(notes: list):  # вивід найменшої за довжиною нотатки
    print(min(notes))


def longest(notes: list):  # вивід найбільшої за довжиною нотатки
    print(max(notes))


def start(notes):  # функція, яка отримує список і маніпулює з ним
    command = get_command()
    if command == 'add':
        add(notes)
        print(notes)
    elif command == 'earliest':
        earliest(notes)
    elif command == 'latest':
        latest(notes)
    elif command == 'longest':
        longest(notes)
    elif command == 'shortest':
        shortest(notes)
    else:
        print('Try again')


if __name__ == '__main__':
    commands = [    # список команди у записнику
        'add',
        'earliest',
        'latest',
        'longest',
        'shortest'
    ]
    show_commands(commands)
    notes = []
    while True:
        start(notes)



