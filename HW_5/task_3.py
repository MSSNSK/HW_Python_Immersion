# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def fibonacci(num):
    prefix_fib = '0, 1'
    start = 1
    fib_1 = 0
    fib_2 = 1
    if num == 0:
        yield '0'
    elif num == 1:
        yield prefix_fib
    elif num == 2:
        yield '0, 1, 1'
    else:
        yield prefix_fib
        for i in range(start, num):
            fib_sum = fib_1 + fib_2
            fib_1, fib_2 = fib_2, fib_sum
            yield fib_sum


fib_num = int(input("Введите число: "))
print(*fibonacci(fib_num), sep=', ')
