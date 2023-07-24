class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print(self):
        for row in self.matrix:
            print(*row)

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix):
            return False
        for row in range(len(self.matrix)):
            if len(self.matrix[row]) != len(other.matrix[row]):
                return False
        return True

    def __add__(self, other):
        if self.matrix == other.matrix:
            new_matrix = []
            for row in range(len(self.matrix)):
                new_matrix.append([*map(lambda x: sum(x), zip(self.matrix[row], other.matrix[row]))])
            return new_matrix
        return False

    def __mul__(self, other):
        if len(self.matrix[0]) == len(other.matrix):
            new_matrix = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return new_matrix
        return False

    def __pow__(self, power):
        matrix: list = self.matrix.copy()

        for i in range(power - 1):
            temp = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        temp[i][j] += self.matrix[i][k] * self.matrix[k][j]
            matrix = temp.copy()
        return matrix
