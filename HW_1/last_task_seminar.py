# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


def multiplication_table():
    LOWER_LIMIT = 2
    UPPER_LIMIT = 10
    COLUMN = 4

    for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN):
        for j in range(LOWER_LIMIT, UPPER_LIMIT + 1):
            for k in range(i, i + COLUMN):
                if j == UPPER_LIMIT and k == i + COLUMN - 1:
                    print(f'{k:>} X {j:>2} = {k * j:>2}\n\n', end='')
                elif k == i + COLUMN - 1:
                    print(f'{k:>} X {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} X {j:>2} = {k * j:>2}\t\t', end='')


multiplication_table()
