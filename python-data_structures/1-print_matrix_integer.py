def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ["{:d}".format(num) for num in row]
        print(" ".join(formatted_row))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
if __name__ == "__main":
 print_matrix_integer(matrix)

