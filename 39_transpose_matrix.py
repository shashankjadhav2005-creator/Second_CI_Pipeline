def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    return [[matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("Original matrix:", matrix)
    print("Transposed matrix:", transpose_matrix(matrix))
