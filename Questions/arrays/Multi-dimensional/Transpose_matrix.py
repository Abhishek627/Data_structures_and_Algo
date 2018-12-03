'''
Transpose means changing rows<---> columns.

'''

def transpose_matrix(matrix):
    col_size = len(matrix[0])
    row_size = len(matrix)

    for i in xrange(row_size):
        for j in xrange(col_size):
            if i < j and matrix[i][j] != matrix[j][i]:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    input_array= [[1,2,3],[4,5,6],[7,8,9]]
    transpose_matrix(input_array)
    print input_array
    assert input_array,[[1,4,7],[2,5,8],[3,6,9]]