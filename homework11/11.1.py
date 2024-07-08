matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
temp = matrix
transposed_matrix = temp


for raw in range(len(matrix)):
    for column in range(len(matrix[raw])):
        transposed_matrix[raw][column] =  matrix[column][raw]

print(transposed_matrix)
