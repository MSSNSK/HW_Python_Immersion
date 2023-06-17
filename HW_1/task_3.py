# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:
#
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint
import sys


lower_limit = 0
upper_limit = 1000
num = randint(lower_limit, upper_limit)
range_attempts = 10

while range_attempts != 0:
    user_num = int(input('Введите число: '))
    if user_num > num:
        range_attempts -= 1
        upper_limit = user_num - 1
        print(f'МЕНЬШЕ! Осталось {range_attempts} попыток.',
              f'Искомое число в диапазоне от {lower_limit} по {upper_limit}',
              '*** для большей эффективности рекомендуется выбирать среднее значение из диапазона ***', sep='\n')
    elif user_num < num:
        range_attempts -= 1
        lower_limit = user_num + 1
        print(f'БОЛЬШЕ! Осталось {range_attempts} попыток.',
              f'Искомое число в диапазоне от {lower_limit} по {upper_limit}',
              '*** для большей эффективности рекомендуется выбирать среднее значение из диапазона ***', sep='\n')
    else:
        print('БИНГО!!!')
        sys.exit()
print(f'ИГРА ОКОНЧЕНА! ВЫ ПРОИГРАЛИ! (было загадано число {num}).')
