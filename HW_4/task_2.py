# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def params_to_dict(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if v.__hash__:
            result[v] = k
        else:
            result[v.__str__()] = k
    return result


print(params_to_dict(frst='one', scnd=2, thrd=[3, 4]))


# ***ДРУГОЙ ВАРИАНТ***


def params_to_dict(**kwargs):
    result = {}
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k
    return result


print(params_to_dict(frst='one', scnd=2, thrd=[3, 4]))


