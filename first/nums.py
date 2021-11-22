# Урок по git: https://www.youtube.com/watch?v=9VKKZNqzPcE

def plus(_a, _b):
    return 10 + _a + _b


def minus(_a, _b):
    return _a - _b


if __name__ == "__main__":
    a, b = 2, 3
    s = plus(a, b)
    expected = 5
    test = 'OK' if s == expected else 'FAIL'
    print(f'Test: plus({a},{b})={s} {test}')
