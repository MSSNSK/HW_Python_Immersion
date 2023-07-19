# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.depth = depth
        self.type = self.check_type()

    def check_type(self):
        return ("Мелководная", "Глубоководная")[self.depth > 1000]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nГлубина: {self.depth}\nТип: {self.type}\n'


class Bird(Animal):
    def __init__(self, name, age, wings):
        super().__init__(name, age)
        self.wings = wings
        self.type = self.check_type()

    def check_type(self):
        return ("Небольшой размах", "Большой размах")[self.wings > 3]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nРазмах крыльев: {self.wings}\nТип: {self.type}\n'


class Mammals(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
        self.type = self.check_type()

    def check_type(self):
        return ("Мелкий", "Крупный")[self.weight > 100]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВес: {self.weight}\nТип: {self.type}\n'


if __name__ == '__main__':
    f = Fish('Дори', 2, 100)
    b = Bird('Кеша', 5, 4)
    m = Mammals('Дамбо', 10, 105)

    print(f)
    print(b)
    print(m)