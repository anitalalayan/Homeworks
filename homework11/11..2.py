matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]


rotated_matrix = [[matrix[raw][column] for column in range(len(matrix) - 1, -1, -1)] for raw in range(len(matrix) - 1, -1, -1)]


print("Matrix rotated by 180 degrees:", end="\n\n")

for i in rotated_matrix:
    print(i)
    







# for raw in range(len(matrix) - 1, -1, -1):
#     for column in range(len(matrix) - 1, -1, -1):
#         print(matrix[raw][column], end=" ")
#     print(" ")


