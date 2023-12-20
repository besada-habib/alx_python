def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ' '.join('{:2d}'.format(element) for element in row)
        print(row_str)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
if __name__ = "__main__":
print_matrix_integer(matrix)