# Возьмите любую из задач с прошлых семинаров.
# Превратите функции в методы класса, а параметры - в свойства.
# Задача должна решаться через вызов методов экземпляра.


import sys


class ATM:
    def __init__(self, balance, operations_count):
        self.balance = balance
        self.operations_count = operations_count

    def print_balance(self):
        print(f'Ваш баланс равен {self.balance}')

    @staticmethod
    def general_processing(func):
        def wrapper(self, amount):
            if amount % 50 == 0:
                func(self, amount)
                self.operations_count += 1
                if self.operations_count % 3 == 0:
                    self.balance += self.balance * 0.03
                if self.balance > 5000000:
                    self.balance -= self.balance * 0.1
                self.print_balance()
            else:
                print('Недопустимая сумма! Сумма должна быть кратна 50!')
        return wrapper

    @general_processing
    def top_up(self, amount):
        self.balance += amount

    @general_processing
    def withdraw(self, amount):
        if amount <= self.balance:
            fee = amount * 0.015
            if fee < 30:
                fee = 30
            elif fee > 600:
                fee = 600
            if self.balance - amount - fee > 0:
                self.balance -= amount + fee
            else:
                self.operations_count -= 1
                print('Операция отменена! Баланс не может быть меньше нуля!')
        else:
            print('Недостаточный баланс!')

    @staticmethod
    def exit():
        print('Хорошего дня!')
        sys.exit()

    def run(self):
        while True:
            print('\n\33[7m' + 'ГЛАВНОЕ МЕНЮ' + '\033[0m\n\n'
                                             '1 - Пополнить\n'
                                             '2 - Снять\n'
                                             '3 - Закончить\n')
            choice = input('Выберите действие: ')
            if choice == "1":
                amount = float(input('Введите сумму для пополнения счета: '))
                self.top_up(amount)
            elif choice == "2":
                amount = float(input('Введите сумму для снятия со счета: '))
                self.withdraw(amount)
            elif choice == "3":
                self.exit()
            else:
                print('Некорректный ввод! Пожалуйста, попробуйте снова!')


bank_account = ATM(0, 0)
bank_account.run()