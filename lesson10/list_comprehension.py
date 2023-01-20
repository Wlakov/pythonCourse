def readfile(filename: str):
    """
    Функція, яка відкриває файл і читає його по рядку і якщо в рядку є маленька 'а', то у рядку прибирається '\n',
    текст строки до першої малої літери "а" і перша літера строки велика, інші - малі
    :param filename: файл, який читаємо
    :return:
    """
    with open(filename, mode='r') as f:
        rr = [line.strip()[line.find('a'):].title() if line.find('a') != -1 else line.replace(line, '')
              for line in f.readlines()]
        print(rr)


if __name__ == '__main__':
    readfile('file.txt')
