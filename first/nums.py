# Урок по git: https://www.youtube.com/watch?v=9VKKZNqzPcE
# unittest: https://www.youtube.com/watch?v=YD7aYJh3k-w
# doctest + unittest: https://www.youtube.com/watch?v=K_BGJx2wxWw
import doctest


def plus(arg_a, arg_b):
    """
    Возвращает сумму аргументов

    :param arg_a:
    :param arg_b:
    :return:

    >>> plus(1,2)
    3
    >>> plus(10,5)
    15
    """
    return arg_a + arg_b


def minus(a, b):
    return a - b


def div(a, b):
    if b == 0:
        raise ValueError("Делитель равен 0")
    return a // b


def round20(x):
    x20 = x * 20
    result = (x // 20) * 20
    if (x % 20) >= 10:
        result += 20
    print(f"round20() x={x} x20={x20} result={result}")
    return result


if __name__ == "__main__":
    arg1, arg2 = 2, 3
    res = plus(arg1, arg2)
    expected = 5
    test = 'OK' if res == expected else 'FAIL'
    print(f'Test: plus({arg1},{arg2})={res} {test}')
    assert (plus(2, 3) == 5)
    doctest.testmod()
    round20(239808)
    round20(239801)
    round20(239810)
    round20(239811)
    round20(239838)

