# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


from fractions import Fraction

def euclid_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_fraction(num, denom):
    egcd_num = euclid_gcd(num, denom)
    if num % denom == 0:
        return num // egcd_num
    return f"{num // egcd_num}/{denom // egcd_num}"

def sum_fractions(nf_1, df_1, nf_2, df_2):
    nf1, df1 = nf_1 * df_2, df_1 * df_2
    nf2, df2 = nf_2 * df_1, df_2 * df_1
    sum_num = nf1 + nf2
    return check_fraction(sum_num, df2)

def mult_fractions(nf_1, df_1, nf_2, df_2):
    mult_nf = nf_1 * nf_2
    mult_df = df_1 * df_2
    return check_fraction(mult_nf, mult_df)


num_fract_1, denom_fract_1 = map(int, input('Введите первую дробь: ').split('/'))
num_fract_2, denom_fract_2 = map(int, input('Введите вторую дробь: ').split('/'))

print(f'''
Сумма дробей: {sum_fractions(num_fract_1, denom_fract_1, num_fract_2, denom_fract_2)}
Проверка суммы: {Fraction(num_fract_1, denom_fract_1) + Fraction(num_fract_2, denom_fract_2)}
 
Произведение дробей: {mult_fractions(num_fract_1, denom_fract_1, num_fract_2, denom_fract_2)}
Проверка: {Fraction(num_fract_1, denom_fract_1) * Fraction(num_fract_2, denom_fract_2)}''')
