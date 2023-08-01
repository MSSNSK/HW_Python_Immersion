# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_num():
    while True:
        try:
            inp = float(input("Введите число: "))
        except ValueError:
            print("Неверное число")
        else:
            if inp * 10 % 10 == 0:
                return int(inp)
            return inp


print(get_num())