# Создайте класс Матрица.
# Добавьте методы для:
# вывода на печать,
# проверку на равенство,
# сложения,
# *умножения матриц
# **Возведение матрицы в степень


from matrix_class import Matrix

m1_prefill = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
m2_prefill = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
m1 = Matrix(m1_prefill)
m2 = Matrix(m2_prefill)
print(m1 ** 2)
