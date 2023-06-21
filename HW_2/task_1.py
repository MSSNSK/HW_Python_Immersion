# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

CONST_HEX = 16
def hex_num(num: int, prod: int) -> str:
    HEX_NUMBERS = '0123456789abcdef'
    HEX_PREFIX = ['0x']
    result = []
    while num > 0:
        num, remainder = divmod(num, prod)
        result.append(str(HEX_NUMBERS[remainder]))
    return ''.join(HEX_PREFIX + result[::-1])


number: int = int(input('Введите число: '))
num_hex: str = hex_num(number, CONST_HEX)

print(f'''
Число: {number}

Шестнадцатеричное представление: {num_hex}
Проверочное: {hex(number)}''')
