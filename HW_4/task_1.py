# Напишите функцию для транспонирования матрицы.


def transposition_matrix(lst):
    for i in range(len(lst)):
        for j in range(i, len((lst[i]))):
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposition_matrix(matrix)
print(*matrix, sep='\n')
