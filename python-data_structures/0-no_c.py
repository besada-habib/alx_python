def no_c(input_string):
    result_string = ''.join(char for char in input_string if char not in ('c', 'C'))
    return result_string

input_str = "Holberton School"
output_str = no_c(input_str)
if __name__ == "__main__":
 print(output_str)