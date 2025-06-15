class DiagonalMatrix:
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    @classmethod
    def sum_of_diagonal_matrix(cls):
        diagonal_sum = sum(cls.matrix[i][i] for i in range(3))
        return diagonal_sum

if __name__ == "__main__":
    obj = DiagonalMatrix()
    result = obj.sum_of_diagonal_matrix()
    print(result)

