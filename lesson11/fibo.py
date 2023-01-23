def fib_gen(n: int):
    """
    Функція-генератор послідовності чисел Фібоначчі
    :param n:кінцевий індекс елементу до якого треба генерувати числа за правилами послідовності Фібоначчі
    :return:число
    """
    fib1 = 1
    fib2 = 0
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        yield fib2


if __name__ == '__main__':
    for x in fib_gen(10):
        print(x)

