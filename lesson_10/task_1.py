class Matrix:
    def __init__(self, numbers):
        self.matrix = numbers

    def __str__(self):
        result = ''
        for i in self.matrix:
            print(i)
        return result

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix)):
            items = []
            for _i in range(len(self.matrix[i])):
                items.append(self.matrix[i][_i] + other.matrix[i][_i])
            matrix_sum.append(items)
        return Matrix(matrix_sum)


matrix_1 = Matrix([[47, -5], [28, 96], [-25, -98]])
matrix_2 = Matrix([[-17, 59], [65, 15], [-9, -69]])

print(matrix_1 + matrix_2)
