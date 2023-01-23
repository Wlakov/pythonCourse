def word_gen(s: str):
    """
    Функція, яка розділяє рядок по словах
    :param s: рядок, який треба розділити по словах
    :return: слово
    """
    for w in s.split():
        yield w


if __name__ == '__main__':
    for word in word_gen('i am generating words from text'):
        print(word)
